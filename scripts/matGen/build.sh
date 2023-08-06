#!/bin/bash -x

ml Stages/2023 GCC OpenMPI imkl CMake Boost git

git clone https://github.com/SimLabQuantumMaterials/DEMAGIS.git

cd DEMAGIS

mkdir build

cd build

cmake .. 

make -j

