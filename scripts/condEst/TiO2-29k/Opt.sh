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

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

export CHASE_DISPLAY_BOUNDS=1

OPT=S
executable=../ChASE/build/examples/2_input_output/2_input_output_mgpu

srun --threads-per-core=1 ${executable} --n 29528 --nev 2560 --nex 400 --path_in=${DATA_PATH}/TiO2-29k/gmat\ \ 1\ \ 1.bin --complex 1 --opt ${OPT} --mode R  --deg 20 --lanczosIter 40 --numLanczos 10 --tol 1e-10

