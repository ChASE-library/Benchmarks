#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=12
#SBATCH --output=Opt.out
#SBATCH --error=Opt.err
#SBATCH --time=1:30:00
#SBATCH --partition=develbooster --gres=gpu:4

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

export CHASE_DISPLAY_BOUNDS=1

OPT=S
executable=../ChASE/build/examples/2_input_output/2_input_output_mgpu

srun --threads-per-core=1 ${executable} --n 62681 --nev 100 --nex 100 --path_in=${DATA_PATH}/HfO2-62k/mat_d_00_01.bin --complex 1 --opt ${OPT} --mode R  --deg 20 --lanczosIter 40 --numLanczos 10 --tol 1e-10


