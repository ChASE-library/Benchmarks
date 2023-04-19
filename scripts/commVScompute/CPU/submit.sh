#!/bin/bash -x

cd v1.2

for file in 1 4 16 64
do
    cd ${file}	
    sbatch submit.sh
    cd ..
done

cd ../v1.3

for file in 1 4 16 64
do
    cd ${file}
    sbatch submit.sh
    cd ..
done

