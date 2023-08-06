#!/bin/bash -x

output=../../../results/hhQR_vs_CholQR_gpu.csv

if test -f "$output"; then
    rm -rf $output
fi

data1=$(grep -hr " |    16 |" NaCl-9k/hhQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/NaCl 9k,HHQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

data2=$(grep -hr " |    16 |" NaCl-9k/cholQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/NaCl 9k,CholeskyQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

echo -e "$data1" >> $output
echo -e "$data2" >> $output

data1=$(grep -hr " |    16 |" TiO2-29k/hhQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/TiO2 29k,HHQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

data2=$(grep -hr " |    16 |" TiO2-29k/cholQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/TiO2 29k,CholeskyQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

echo -e "$data1" >> $output
echo -e "$data2" >> $output

data1=$(grep -hr " |    16 |" AuAg-13k/hhQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/AuAg 13k,HHQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

data2=$(grep -hr " |    16 |" AuAg-13k/cholQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/AuAg 13k,CholeskyQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

echo -e "$data1" >> $output
echo -e "$data2" >> $output

data1=$(grep -hr " |    16 |" HfO2-76k/hhQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/HfO2 76k,HHQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

data2=$(grep -hr " |    16 |" HfO2-76k/cholQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/HfO2 76k,CholeskyQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

echo -e "$data1" >> $output
echo -e "$data2" >> $output

data1=$(grep -hr " |    16 |" In2O3-76k/hhQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/In2O3 76k,HHQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

data2=$(grep -hr " |    16 |" In2O3-76k/cholQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/In2O3 76k,CholeskyQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

echo -e "$data1" >> $output
echo -e "$data2" >> $output

data1=$(grep -hr " |    16 |" In2O3-115k/hhQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/In2O3 115k,HHQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

data2=$(grep -hr " |    16 |" In2O3-115k/cholQR.out | tr -d " \t\r" | tr '|' ',' | sed -e 's/^/In2O3 115k,CholeskyQR/' | sed 's/.$//' | cut -d, -f1-2,6-7,8,11)

echo -e "$data1" >> $output
echo -e "$data2" >> $output

sed -i -e '1s/^/Type,QR Impl,Iters.,MatVecs,All(s),QR(s)\
/' $output 

if test -f "$output-e"; then
    rm -rf $output-e
fi

