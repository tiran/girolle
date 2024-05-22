# Girolle - Tête de Moine cheese wheels

Girolle takes a wheel and turns it into a Fedora wheel with RPM requirements.

## Example
```shell
$ girolle torch-2.3.0-cp312-cp312-manylinux1_x86_64.whl
INFO:girolle.girolle:os tag: fc39, machine: x86_64
DEBUG:girolle.girolle:Wheel torch-2.3.0-cp312-cp312-manylinux1_x86_64.whl has so files: functorch/_C.cpython-312-x86_64-linux-gnu.so, torch/_C.cpython-312-x86_64-linux-gnu.so, torch/lib/libc10.so, torch/lib/libc10_cuda.so, torch/lib/libcaffe2_nvrtc.so, torch/lib/libshm.so, torch/lib/libtorch.so, torch/lib/libtorch_cpu.so, torch/lib/libtorch_cuda.so, torch/lib/libtorch_cuda_linalg.so, torch/lib/libtorch_global_deps.so, torch/lib/libtorch_python.so
DEBUG:girolle.girolle:RPM requires: ld-linux-x86-64.so.2()(64bit), ld-linux-x86-64.so.2(GLIBC_2.3)(64bit), libc.so.6()(64bit), libc.so.6(GLIBC_2.10)(64bit), libc.so.6(GLIBC_2.11)(64bit), libc.so.6(GLIBC_2.14)(64bit), libc.so.6(GLIBC_2.16)(64bit), libc.so.6(GLIBC_2.2.5)(64bit), libc.so.6(GLIBC_2.3)(64bit), libc.so.6(GLIBC_2.3.2)(64bit), libc.so.6(GLIBC_2.3.4)(64bit), libc.so.6(GLIBC_2.4)(64bit), libc.so.6(GLIBC_2.6)(64bit), libc.so.6(GLIBC_2.7)(64bit), libc.so.6(GLIBC_2.9)(64bit), libcublas.so.12()(64bit), libcublas.so.12(libcublas.so.12)(64bit), libcublasLt.so.12()(64bit), libcublasLt.so.12(libcublasLt.so.12)(64bit), libcuda.so.1()(64bit), libcudart.so.12()(64bit), libcudart.so.12(libcudart.so.12)(64bit), libcudnn.so.8()(64bit), libcudnn.so.8(libcudnn.so.8)(64bit), libcufft.so.11()(64bit), libcufft.so.11(libcufft.so.11)(64bit), libcupti.so.12()(64bit), libcupti.so.12(libcupti.so.12)(64bit), libcurand.so.10()(64bit), libcusolver.so.11()(64bit), libcusolver.so.11(libcusolver.so.11)(64bit), libcusparse.so.12()(64bit), libcusparse.so.12(libcusparse.so.12)(64bit), libcusparseLt-f80c68d1.so.0()(64bit), libdl.so.2()(64bit), libdl.so.2(GLIBC_2.2.5)(64bit), libdl.so.2(GLIBC_2.3.3)(64bit), libgcc_s.so.1()(64bit), libgcc_s.so.1(GCC_3.0)(64bit), libgcc_s.so.1(GCC_3.4)(64bit), libgomp-a34b3233.so.1()(64bit), libgomp-a34b3233.so.1(GOMP_1.0)(64bit), libgomp-a34b3233.so.1(GOMP_4.0)(64bit), libgomp-a34b3233.so.1(OMP_1.0)(64bit), libm.so.6()(64bit), libm.so.6(GLIBC_2.2.5)(64bit), libnccl.so.2()(64bit), libnvToolsExt.so.1()(64bit), libnvToolsExt.so.1(libnvToolsExt.so.1)(64bit), libnvrtc.so.12()(64bit), libnvrtc.so.12(libnvrtc.so.12)(64bit), libpthread.so.0()(64bit), libpthread.so.0(GLIBC_2.12)(64bit), libpthread.so.0(GLIBC_2.2.5)(64bit), libpthread.so.0(GLIBC_2.3.2)(64bit), libpthread.so.0(GLIBC_2.3.3)(64bit), librt.so.1()(64bit), librt.so.1(GLIBC_2.2.5)(64bit), libstdc++.so.6()(64bit), libstdc++.so.6(CXXABI_1.3)(64bit), libstdc++.so.6(CXXABI_1.3.2)(64bit), libstdc++.so.6(CXXABI_1.3.3)(64bit), libstdc++.so.6(CXXABI_1.3.5)(64bit), libstdc++.so.6(CXXABI_1.3.7)(64bit), libstdc++.so.6(GLIBCXX_3.4)(64bit), libstdc++.so.6(GLIBCXX_3.4.11)(64bit), libstdc++.so.6(GLIBCXX_3.4.13)(64bit), libstdc++.so.6(GLIBCXX_3.4.14)(64bit), libstdc++.so.6(GLIBCXX_3.4.15)(64bit), libstdc++.so.6(GLIBCXX_3.4.17)(64bit), libstdc++.so.6(GLIBCXX_3.4.18)(64bit), libstdc++.so.6(GLIBCXX_3.4.19)(64bit), libstdc++.so.6(GLIBCXX_3.4.5)(64bit), libstdc++.so.6(GLIBCXX_3.4.9)(64bit), rtld(GNU_HASH)
DEBUG:girolle.girolle:Skipped: libc10.so()(64bit), libc10_cuda.so()(64bit), libshm.so()(64bit), libtorch.so()(64bit), libtorch_cpu.so()(64bit), libtorch_cuda.so()(64bit), libtorch_python.so()(64bit)
DEBUG:girolle.girolle:Detected CUDA library: libcudart.so.12()(64bit) (version: 12)
INFO:auditwheel.wheeltools:Previous filename tags: manylinux1_x86_64
INFO:auditwheel.wheeltools:New filename tags: fc39-x86_64-cu12
INFO:auditwheel.wheeltools:Previous WHEEL info tags: cp312-cp312-linux_x86_64
INFO:auditwheel.wheeltools:New WHEEL info tags: cp312-cp312-fc39-x86_64-cu12

torch-2.3.0-cp312-cp312-fc39-x86_64-cu12.whl
```

```shell
$ unzip torch-2.3.0-cp312-cp312-fc39-x86_64-cu12.whl torch-2.3.0.dist-info/rpm-requires.txt
Archive:  torch-2.3.0-cp312-cp312-fc39-x86_64-cu12.whl
  inflating: torch-2.3.0.dist-info/rpm-requires.txt

$ cat torch-2.3.0.dist-info/rpm-requires.txt
ld-linux-x86-64.so.2()(64bit)
ld-linux-x86-64.so.2(GLIBC_2.3)(64bit)
libc.so.6()(64bit)
libc.so.6(GLIBC_2.10)(64bit)
libc.so.6(GLIBC_2.11)(64bit)
libc.so.6(GLIBC_2.14)(64bit)
libc.so.6(GLIBC_2.16)(64bit)
libc.so.6(GLIBC_2.2.5)(64bit)
libc.so.6(GLIBC_2.3)(64bit)
libc.so.6(GLIBC_2.3.2)(64bit)
libc.so.6(GLIBC_2.3.4)(64bit)
libc.so.6(GLIBC_2.4)(64bit)
libc.so.6(GLIBC_2.6)(64bit)
libc.so.6(GLIBC_2.7)(64bit)
libc.so.6(GLIBC_2.9)(64bit)
libcublas.so.12()(64bit)
libcublas.so.12(libcublas.so.12)(64bit)
libcublasLt.so.12()(64bit)
libcublasLt.so.12(libcublasLt.so.12)(64bit)
libcuda.so.1()(64bit)
libcudart.so.12()(64bit)
libcudart.so.12(libcudart.so.12)(64bit)
libcudnn.so.8()(64bit)
libcudnn.so.8(libcudnn.so.8)(64bit)
libcufft.so.11()(64bit)
libcufft.so.11(libcufft.so.11)(64bit)
libcupti.so.12()(64bit)
libcupti.so.12(libcupti.so.12)(64bit)
libcurand.so.10()(64bit)
libcusolver.so.11()(64bit)
libcusolver.so.11(libcusolver.so.11)(64bit)
libcusparse.so.12()(64bit)
libcusparse.so.12(libcusparse.so.12)(64bit)
libcusparseLt-f80c68d1.so.0()(64bit)
libdl.so.2()(64bit)
libdl.so.2(GLIBC_2.2.5)(64bit)
libdl.so.2(GLIBC_2.3.3)(64bit)
libgcc_s.so.1()(64bit)
libgcc_s.so.1(GCC_3.0)(64bit)
libgcc_s.so.1(GCC_3.4)(64bit)
libgomp-a34b3233.so.1()(64bit)
libgomp-a34b3233.so.1(GOMP_1.0)(64bit)
libgomp-a34b3233.so.1(GOMP_4.0)(64bit)
libgomp-a34b3233.so.1(OMP_1.0)(64bit)
libm.so.6()(64bit)
libm.so.6(GLIBC_2.2.5)(64bit)
libnccl.so.2()(64bit)
libnvToolsExt.so.1()(64bit)
libnvToolsExt.so.1(libnvToolsExt.so.1)(64bit)
libnvrtc.so.12()(64bit)
libnvrtc.so.12(libnvrtc.so.12)(64bit)
libpthread.so.0()(64bit)
libpthread.so.0(GLIBC_2.12)(64bit)
libpthread.so.0(GLIBC_2.2.5)(64bit)
libpthread.so.0(GLIBC_2.3.2)(64bit)
libpthread.so.0(GLIBC_2.3.3)(64bit)
librt.so.1()(64bit)
librt.so.1(GLIBC_2.2.5)(64bit)
libstdc++.so.6()(64bit)
libstdc++.so.6(CXXABI_1.3)(64bit)
libstdc++.so.6(CXXABI_1.3.2)(64bit)
libstdc++.so.6(CXXABI_1.3.3)(64bit)
libstdc++.so.6(CXXABI_1.3.5)(64bit)
libstdc++.so.6(CXXABI_1.3.7)(64bit)
libstdc++.so.6(GLIBCXX_3.4)(64bit)
libstdc++.so.6(GLIBCXX_3.4.11)(64bit)
libstdc++.so.6(GLIBCXX_3.4.13)(64bit)
libstdc++.so.6(GLIBCXX_3.4.14)(64bit)
libstdc++.so.6(GLIBCXX_3.4.15)(64bit)
libstdc++.so.6(GLIBCXX_3.4.17)(64bit)
libstdc++.so.6(GLIBCXX_3.4.18)(64bit)
libstdc++.so.6(GLIBCXX_3.4.19)(64bit)
libstdc++.so.6(GLIBCXX_3.4.5)(64bit)
libstdc++.so.6(GLIBCXX_3.4.9)(64bit)
rtld(GNU_HASH)
```
