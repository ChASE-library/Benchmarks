#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=4
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=1:30:00
#SBATCH --partition=develbooster --gres=gpu:4

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

for i in {1..15}
do
srun --threads-per-core=1 ../elpa_miniapp/build/elpa.exe 115459 1200 16 ${DATA_PATH}/In2O3-115k/mat.bin

ELPA_MINIAPPS_SOLVER=1 srun --threads-per-core=1 ../elpa_miniapp/build/elpa.exe 115459 1200 16 ${DATA_PATH}/In2O3-115k/mat.bin
done





