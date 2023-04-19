#!/bin/sh

output=../../results/chase_Kernel_comm_vs_compute.csv

if test -f "$output"; then
    rm -rf $output
fi

echo "Nodes,Impls,Kernels,Compt.,Comm." >> $output

Impl="ChASEv1.2"
mode="(GPU)"

bash query_v12.sh 1 GPU/v1.2/1/report1.sqlite 1 ${Impl} ${mode} >> $output

bash query_v12.sh 1 GPU/v1.2/4/report1.sqlite 4 ${Impl} ${mode} >> $output

bash query_v12.sh 1 GPU/v1.2/16/report1.sqlite 16 ${Impl} ${mode} >> $output

bash query_v12.sh 1 GPU/v1.2/64/report1.sqlite 64 ${Impl} ${mode} >> $output

Impl="ChASEv1.2"
mode="(CPU)"
bash query_v12.sh 16 CPU/v1.2/1/report1.sqlite 1 ${Impl} ${mode} >> $output

bash query_v12.sh 16 CPU/v1.2/4/report1.sqlite 4 ${Impl} ${mode} >> $output

bash query_v12.sh 16 CPU/v1.2/16/report1.sqlite 16 ${Impl} ${mode} >> $output

bash query_v12.sh 16 CPU/v1.2/64/report1.sqlite 64 ${Impl} ${mode} >> $output

Impl="ChASEv1.3"
mode="(GPU)"

bash query_v13.sh 4 GPU/v1.3/1/report1.sqlite 1 ${Impl} ${mode} >> $output

bash query_v13.sh 4 GPU/v1.3/4/report1.sqlite 4 ${Impl} ${mode} >> $output

bash query_v13.sh 4 GPU/v1.3/16/report1.sqlite 16 ${Impl} ${mode} >> $output

bash query_v13.sh 4 GPU/v1.3/64/report1.sqlite 64 ${Impl} ${mode} >> $output

Impl="ChASEv1.3"
mode="(CPU)"
bash query_v13.sh 16 CPU/v1.3/1/report1.sqlite 1 ${Impl} ${mode} >> $output

bash query_v13.sh 16 CPU/v1.3/4/report1.sqlite 4 ${Impl} ${mode} >> $output

bash query_v13.sh 16 CPU/v1.3/16/report1.sqlite 16 ${Impl} ${mode} >> $output

bash query_v13.sh 16 CPU/v1.3/64/report1.sqlite 64 ${Impl} ${mode} >> $output

output2=../../results/Initialization_overhead_new.csv
if test -f "$output2"; then
    rm -rf $output2
fi
echo "Nodes,Impls,Kernels,Random Generation,Others" >> $output2
Impl="ChASEv1.3"
mode="(GPU)"

bash query_init_v13.sh 4 GPU/v1.3/1/report1.sqlite 1 ${Impl} ${mode} >> $output2

bash query_init_v13.sh 4 GPU/v1.3/4/report1.sqlite 4 ${Impl} ${mode} >> $output2

bash query_init_v13.sh 4 GPU/v1.3/16/report1.sqlite 16 ${Impl} ${mode} >> $output2

bash query_init_v13.sh 4 GPU/v1.3/64/report1.sqlite 64 ${Impl} ${mode} >> $output2

Impl="ChASEv1.3"
mode="(CPU)"
bash query_init_v13.sh 16 CPU/v1.3/1/report1.sqlite 1 ${Impl} ${mode} >> $output2

bash query_init_v13.sh 16 CPU/v1.3/4/report1.sqlite 4 ${Impl} ${mode} >> $output2

bash query_init_v13.sh 16 CPU/v1.3/16/report1.sqlite 16 ${Impl} ${mode} >> $output2

bash query_init_v13.sh 16 CPU/v1.3/64/report1.sqlite 64 ${Impl} ${mode} >> $output2

output3=../../results/Initialization_overhead_old.csv
if test -f "$output3"; then
    rm -rf $output3
fi
echo "Nodes,Impls,Kernels,Random Generation,Others" >> $output3
Impl="ChASEv1.2"
mode="(GPU)"

bash query_init_v12.sh 1 GPU/v1.2/1/report1.sqlite 1 ${Impl} ${mode} >> $output3

bash query_init_v12.sh 1 GPU/v1.2/4/report1.sqlite 4 ${Impl} ${mode} >> $output3

bash query_init_v12.sh 1 GPU/v1.2/16/report1.sqlite 16 ${Impl} ${mode} >> $output3

bash query_init_v12.sh 1 GPU/v1.2/64/report1.sqlite 64 ${Impl} ${mode} >> $output3

Impl="ChASEv1.2"
mode="(CPU)"
bash query_init_v12.sh 4 CPU/v1.2/1/report1.sqlite 1 ${Impl} ${mode} >> $output3

bash query_init_v12.sh 4 CPU/v1.2/4/report1.sqlite 4 ${Impl} ${mode} >> $output3

bash query_init_v12.sh 4 CPU/v1.2/16/report1.sqlite 16 ${Impl} ${mode} >> $output3

bash query_init_v12.sh 4 CPU/v1.2/64/report1.sqlite 64 ${Impl} ${mode} >> $output3


