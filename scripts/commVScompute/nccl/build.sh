#!/bin/bash -x

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

mkdir build

cd build

cmake ../../ChASE-v1.3 -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release

make -j


