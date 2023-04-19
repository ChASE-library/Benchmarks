#!/bin/bash -x

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

mkdir ChASE_v12

cd ChASE_v12

mkdir build

cd build

cmake ../../../ChASE-v1.2  -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_NSIGHT=ON

make -j

