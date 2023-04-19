#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=64
#SBATCH --ntasks=1024
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=24:00:00
#SBATCH --partition=dc-cpu

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

srun -n 900 --threads-per-core=1 ../DEMAGIS/build/examples/driver_scalapack.exe --N 210000 --dim0 30 --dim1 30 --mbsize 500 --nbsize 500 --dmax 70 --epsilon=1e-4 --myDist 0

mv *.bin ../../../data/


