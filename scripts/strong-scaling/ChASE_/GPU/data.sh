#!/bin/bash -x

output="../../../../results/chase_gpu_vs_elpa.csv"

if test -f "$output"; then
    rm -rf $output
fi

for file in $(find . -name "*.out")
do
    data=$(grep "| Size  | Iterations |" -A1 ${file} | grep -v "| Size  | Iterations |" | sed '/^--$/d' | tr -d " \t\r" | tr '|' ',' | sed -e "s/^/ChASE-GPU (v1.3.1),$(basename $(dirname ${file}))/" | sed 's/.$//')
    echo -e "$data" >> $output
done

sed -i -e '1s/^/solver,nodes,GFLOPS,GFLOPS(F),nprocs,Iterations,Vecs,All[sec],Lanczos[sec],Filter[sec],QR[sec],RR[sec],Resid[sec]\
/' $output

if test -f "$output-e"; then
    rm -rf $output-e
fi


