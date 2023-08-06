#!/bin/bash -x

cd 1

sbatch submit.sh

cd ..

cd 4

sbatch submit.sh

cd ..

cd 16

sbatch submit.sh

cd ..

cd 64

sbatch submit.sh

cd ..

