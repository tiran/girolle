# SPDX-License-Identifier: Apache-2.0
import argparse
import logging
import os
import platform
import re
import subprocess
import typing

from auditwheel.wheeltools import InWheelCtx, _dist_info_dir, add_platforms
from packaging.utils import parse_wheel_filename

logger = logging.getLogger(__name__)

# libcudart.so.12 -> cu12
CUDA_VER = re.compile(r"^libcudart\.so\.(\d+)")


def get_os_tag() -> str:
    osrelease = platform.freedesktop_os_release()
    osid = osrelease["ID"]
    if osid == "fedora":
        return f"fc{osrelease['VERSION_ID']}"
    raise ValueError(osid)


def add_rpm_requires(ctx: InWheelCtx) -> typing.Iterable[str]:
    sofiles = sorted(fname for fname in ctx.iter_files() if fname.endswith(".so"))
    logger.debug(
        "Wheel %s has so files: %s", os.path.basename(ctx.in_wheel), ", ".join(sofiles)
    )
    sonames = tuple(os.path.basename(fname) for fname in sofiles)

    requires = set()
    skipped = set()
    if sofiles:
        cmd = ["/usr/lib/rpm/elfdeps", "--requires"]
        cmd.extend(sofiles)
        output = subprocess.check_output(cmd, text=True)
        for line in output.split("\n"):
            line = line.strip()
            if not line:
                continue
            if line.startswith(sonames):
                skipped.add(line)
            else:
                requires.add(line)

        logger.debug("RPM requires: %s", ", ".join(sorted(requires)))
        logger.debug("Skipped: %s", ", ".join(sorted(skipped)))

        dist_info = _dist_info_dir(ctx.path)
        with open(os.path.join(dist_info, "rpm-requires.txt"), "w") as f:
            for line in sorted(requires):
                f.write(f"{line}\n")
    return requires


def girolle(wheel_fname: str) -> str:
    # can we detect these values from ELF metadata?
    os_tag = get_os_tag()
    machine = platform.machine()
    logger.info("os tag: %s, machine: %s", os_tag, machine)
    target_platform = f"{os_tag}_{machine}"

    _, _, _, in_tags = parse_wheel_filename(wheel_fname)
    in_platforms: list[str] = list(set(t.platform for t in in_tags))

    wheel_fname = os.path.abspath(wheel_fname)

    with InWheelCtx(wheel_fname) as ctx:
        deps = add_rpm_requires(ctx)
        for dep in deps:
            mo = CUDA_VER.match(dep)
            if mo is not None:
                logger.debug(
                    "Detected CUDA library: %s (version: %s)", dep, mo.group(1)
                )
                target_platform += f"-cu{mo.group(1)}"
                break
        ctx.out_wheel = wheel_fname
        ctx.out_wheel = add_platforms(ctx, [target_platform], in_platforms)

    return ctx.out_wheel


def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description="Girolle for wheels")
    parser.add_argument("wheel")

    args = parser.parse_args()
    outfile = girolle(args.wheel)
    print(outfile)


if __name__ == "__main__":
    main()
