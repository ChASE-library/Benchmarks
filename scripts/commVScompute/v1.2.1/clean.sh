#!/bin/sh

for file in $(find . -name "*.out")
do
    echo ${file}
    grep "+ " ${file} > tmp && mv tmp ${file}
done
