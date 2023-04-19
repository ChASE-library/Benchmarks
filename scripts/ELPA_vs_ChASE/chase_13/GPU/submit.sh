#!/bin/bash -x

for node in $(echo $1 | sed "s/,/ /g")
do
    cd ${node}
    sbatch submit.sh
    cd ..
done

