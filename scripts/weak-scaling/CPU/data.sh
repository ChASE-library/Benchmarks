#!/bin/bash -x

output=../../../results/weak-scaling-cpu-old.csv

if test -f "$output"; then
    rm -rf $output
fi

for file in $(find ./v1.2 -name "*.out")
do
    data=$(grep "| Size  | Iterations |" -A1 ${file} | grep -v "| Size  | Iterations |" | sed '/^--$/d' | tr -d " \t\r" | tr '|' ',' | sed -e "s/^/ChASE-CPU (v1.2.1),$(basename $(dirname ${file}))/" | sed 's/.$//')
    echo -e "$data" >> $output	
done

sed -i -e '1s/^/mode,nodes,nprocs,Iterations,Vecs,All[sec],Lanczos[sec],Filter[sec],QR[sec],RR[sec],Resid[sec]\
/' $output

if test -f "$output-e"; then
    rm -rf $output-e
fi

output=../../../results/weak-scaling-cpu-new.csv

if test -f "$output"; then
    rm -rf $output
fi

for file in $(find ./v1.3 -name "*.out")
do
    data=$(grep "| Size  | Iterations |" -A1 ${file} | grep -v "| Size  | Iterations |" | sed '/^--$/d' | tr -d " \t\r" | tr '|' ',' | sed -e "s/^/ChASE-CPU (v1.3.1),$(basename $(dirname ${file}))/" | sed 's/.$//')
    echo -e "$data" >> $output
done

sed -i -e '1s/^/mode,nodes,nprocs,Iterations,Vecs,All[sec],Lanczos[sec],Filter[sec],QR[sec],RR[sec],Resid[sec]\
/' $output 

if test -f "$output-e"; then
    rm -rf $output-e
fi


