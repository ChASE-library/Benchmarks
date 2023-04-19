#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=4
#SBATCH --ntasks=64
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8
#SBATCH --output=hhQR.out
#SBATCH --error=hhQR.err
#SBATCH --time=1:30:00
#SBATCH --partition=dc-cpu-devel

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

executable=../ChASE/build/examples/2_input_output/2_input_output

for i in 1 2 3 4 5
do
CHASE_DISABLE_CHOLQR=1 srun --threads-per-core=1 ${executable} --n 12455 --nev 1076 --nex 100 --path_in=${DATA_PATH}/TiO2-12k/gmat\ \ 1\ \ 1.bin --complex 1 --opt S --mode R  --deg 20 --lanczosIter 40 --numLanczos 10 --tol 1e-10
done






