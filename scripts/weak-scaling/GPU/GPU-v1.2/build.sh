#!/bin/bash -x

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

git clone https://github.com/ChASE-library/ChASE.git ChASE

cd ChASE

git checkout v1.2.1

mkdir build

cd build

cmake .. -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release

make -j

