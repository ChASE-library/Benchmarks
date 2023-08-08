#!/bin/bash -x

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

mkdir build

cd build

cmake ../../ChASE-v1.4 -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_CUDA_AWARE_MPI=OFF

make -j


