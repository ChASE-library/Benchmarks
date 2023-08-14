#!/bin/bash -x

output=../../results/NaCl-9k_Opt1.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" NaCl-9k/Opt.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/NaCl-9k_No_Opt.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" NaCl-9k/OptN.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}


output=../../results/TiO2-29k_Opt1.csv

if test -f "$output"; then
    rm -rf $output
fi


grep -hr "estimate:" TiO2-29k/Opt.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/TiO2-29k_No_Opt.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" TiO2-29k/OptN.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}


output=../../results/AuAg-13k_Opt1.csv

if test -f "$output"; then
    rm -rf $output
fi


grep -hr "estimate:" AuAg-13k/Opt.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/AuAg-13k_No_Opt.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" AuAg-13k/OptN.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}


output=../../results/In2O3-76k_Opt1.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" In2O3-76k/Opt.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/In2O3-76k_No_Opt.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" In2O3-76k/OptN.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/In2O3-115k_Opt1.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" In2O3-115k/Opt.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/In2O3-115k_No_Opt.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" In2O3-115k/OptN.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/HfO2-76k_Opt1.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" HfO2-76k/Opt.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}

output=../../results/HfO2-76k_No_Opt.csv

if test -f "$output"; then
    rm -rf $output
fi

grep -hr "estimate:" HfO2-76k/OptN.out | sed 's/estimate: //' | sed 's/rcond: //' | sed 's/ratio: //' | tr -d " " | nl -w2 -s',' | sed '1s/^/Iteration,estimate,rcond,ratio\
/' | sed 's/^[ \t]*//' > ${output}


