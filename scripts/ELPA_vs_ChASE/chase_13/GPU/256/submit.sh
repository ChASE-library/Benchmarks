#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=256
#SBATCH --ntasks=1024
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=12
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=1:30:00
#SBATCH --partition=booster --gres=gpu:4

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2022 GCC OpenMPI CUDA imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}

OPT=S
executable=../ChASE/build/examples/2_input_output/2_input_output_mgpu

for i in {1..15}
do
srun --threads-per-core=1 ${executable} --n 115459 --nev 1200 --nex 400 --path_in=${DATA_PATH}/In2O3-115k/mat.bin --complex 1 --opt ${OPT} --mode R  --deg 20 --lanczosIter 40 --numLanczos 10 --tol 1e-10
done
