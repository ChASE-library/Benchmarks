#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=16
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=24:00:00
#SBATCH --partition=dc-cpu

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

srun -n 256 --threads-per-core=1 ../DEMAGIS/build/examples/driver_scalapack.exe --N 180000 --dim0 16 --dim1 16 --mbsize 625 --nbsize 625 --dmax 60 --epsilon=1e-4 --myDist 0

mv *.bin ../../../data/


