#!/bin/bash -x

cd v1.2

for node in $(echo $1 | sed "s/,/ /g")
do
    cd ${node}
    sbatch submit.sh
    cd ..
done	

cd ../v1.3

for node in $(echo $1 | sed "s/,/ /g")
do
    cd ${node}	
    sbatch submit.sh
    cd ..
done

