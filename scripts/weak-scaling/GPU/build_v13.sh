#!/bin/bash -x

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

git clone https://github.com/ChASE-library/ChASE.git ChASE_v13

cd ChASE_v13

git checkout v1.3.1

mkdir build

cd build

cmake .. -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release

make -j

