#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=64
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=12
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=1:30:00
#SBATCH --partition=booster --gres=gpu:4

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}
export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

for i in {1..4}
do
srun --threads-per-core=1 ../../ChASE_v12/build/examples/2_input_output/2_input_output_mgpu --n 240000 --path_in=../../../../../data/matgen_m_240000_Uniform_eps_1.000000e-04_dmax_8.000000e+01.bin --nev 2250 --nex 750 --complex 0 --tol 1e-10 --opt S --deg 20 --mode R --maxIter 1
done

