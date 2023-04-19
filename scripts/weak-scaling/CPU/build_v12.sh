#!/bin/bash -x

ml Stages/2022 GCC OpenMPI imkl CMake Boost git

git clone https://github.com/ChASE-library/ChASE.git ChASE_v12

cd ChASE_v12

git checkout v1.2.1

mkdir build

cd build

cmake .. -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release

make -j

