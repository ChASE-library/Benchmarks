#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=64
#SBATCH --ntasks=1024
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=1:30:00
#SBATCH --partition=dc-cpu

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}
export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

nsys profile --trace=nvtx --stats=true srun --threads-per-core=1 ../../ChASE_v12/build/examples/2_input_output/2_input_output --n 240000 --path_in=$DATA_PATH/matgen_m_240000_Uniform_eps_1.000000e-04_dmax_80.bin --nev 2250 --nex 750 --complex 0 --tol 1e-10 --opt S --deg 20 --mode R --maxIter 1

