#!/bin/bash -x

output=../../../results/elpa2_gpu.csv

if test -f "$output"; then
    rm -rf $output
fi

for file in $(find . -name "*.out")
do
    data=$(grep -hr "Solver 2" ${file} | tr -d ">" | sed 's/-Solver 2: //'  | sed -e "s/^/ELPA2-GPU,$(basename $(dirname ${file})),/")
    if [ ! -z "$data" ]
    then
        echo -e "$data" >> $output
    fi
done

sed -i -e '1s/^/solver,nodes,nprocs,nev,time[sec]\
/' $output && rm ${output}-e


output=../../../results/elpa1_gpu.csv

if test -f "$output"; then
    rm -rf $output
fi

for file in $(find . -name "*.out")
do
    data=$(grep -hr "Solver 1" ${file} | tr -d ">" | sed 's/-Solver 1: //'  | sed -e "s/^/ELPA1-GPU,$(basename $(dirname ${file})),/")
    if [ ! -z "$data" ]
    then
        echo -e "$data" >> $output
    fi
done

sed -i -e '1s/^/solver,nodes,nprocs,nev,time[sec]\
/' $output

if test -f "$output-e"; then
    rm -rf $output-e
fi
