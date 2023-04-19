#!/bin/bash -x

for n in $(echo $1 | sed "s/,/ /g")
do
    cd ${n}	
    sbatch matgen.sh
    cd ..
done
