#!/bin/bash -x

ml Stages/2022 GCC OpenMPI imkl CMake Boost git

git clone https://gitlab.mpcdf.mpg.de/elpa/elpa.git

cd elpa

git checkout new_release_2022.11.001.rc1

mkdir build

mkdir install

cd build

../autogen.sh

../configure --enable-openmp --enable-allow-thread-limiting --without-threading-support-check-during-build --disable-avx512 --enable-nvidia-gpu --with-NVIDIA-GPU-compute-capability=sm_80  CC=mpicc CFLAGS="-O3 -march=native -g" FC=mpif90 FCFLAGS="-O3 -g" SCALAPACK_FCFLAGS="-I${MKLROOT}/include/intel64/lp64/" SCALAPACK_LDFLAGS="-L${MKLROOT}/lib/intel64  -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lmkl_blacs_openmpi_lp64 -lpthread -Wl,-rpath,${MKLROOT}/lib/intel64" --prefix=${PWD}/../install

make

make install

cd ../../elpa_miniapp

mkdir build

cd build

cmake ..

make -j


