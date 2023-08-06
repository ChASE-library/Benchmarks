#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=4
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=12
#SBATCH --output=OptN.out
#SBATCH --error=OptN.err
#SBATCH --time=1:30:00
#SBATCH --partition=develbooster --gres=gpu:4

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

export CHASE_DISPLAY_BOUNDS=1

OPT=N
executable=../ChASE/build/examples/2_input_output/2_input_output_mgpu

srun --threads-per-core=1 ${executable} --n 76887 --nev 100 --nex 40 --path_in=${DATA_PATH}/In2O3-76k/mat.bin --complex 1 --opt ${OPT} --mode R  --deg 20 --lanczosIter 40 --numLanczos 10 --tol 1e-10

