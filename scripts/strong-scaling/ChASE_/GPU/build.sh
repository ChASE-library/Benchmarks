#!/bin/bash -x

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

git clone https://github.com/ChASE-library/ChASE.git

cd ChASE

git checkout v1.4.0

mkdir build

cd build

cmake .. -DBUILD_WITH_EXAMPLES=ON -DCMAKE_BUILD_TYPE=Release -DCHASE_OUTPUT=ON -DENABLE_CUDA_AWARE_MPI=OFF

make -j

