#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=49
#SBATCH --ntasks=784
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=8
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=1:30:00
#SBATCH --partition=dc-cpu-devel

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}
export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

for i in {1..4}
do
srun --threads-per-core=1 ../../ChASE_v12/build/examples/2_input_output/2_input_output --n 130000 --path_in=../../../../../data/matgen_m_130000_Uniform_eps_1.000000e-05_dmax_1.000000e+00.bin --nev 1000 --nex 300 --complex 0 --tol 1e-10 --opt S --deg 20 --mode R --maxIter 25 --lanczosIter 40 --numLanczos 10
done

