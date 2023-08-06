#!/bin/bash -x
#SBATCH --account=slai
#SBATCH --nodes=4
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=12
#SBATCH --output=hhQR.out
#SBATCH --error=hhQR.err
#SBATCH --time=1:30:00
#SBATCH --partition=develbooster --gres=gpu:4

export SRUN_CPUS_PER_TASK=${SLURM_CPUS_PER_TASK}

ml Stages/2023 GCC OpenMPI CUDA imkl CMake Boost git

export OMP_NUM_THREADS=${SRUN_CPUS_PER_TASK}
export MKL_NUM_THREADS=1

executable=../ChASE/build/examples/2_input_output/2_input_output_mgpu

for i in 1 2 3 4 5
do
CHASE_DISABLE_CHOLQR=1 srun --threads-per-core=1 ${executable} --n 115459 --nev 100 --nex 40 --path_in=${DATA_PATH}/In2O3-115k/mat.bin --complex 1 --opt S --mode R  --deg 20 --lanczosIter 40 --numLanczos 10 --tol 1e-10
done
