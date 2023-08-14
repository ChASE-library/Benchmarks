# Weak scaling

## Summary

For the weak-scaling experiments of ChASE with GPU build, we employed up to 900 out of 936 compute nodes of the JUWELS-Booster, $3,600$ NVIDIA A100 GPUs in total. The compute nodes count is also here chosen as square integer $1,4,9, \cdots, 121,144,256,400, 625, 900$.

For all weak scaling tests, we used artificial matrices, with a size increment of 30k (30k, 60k, 90k, ...). The maximal matrix size tested is 900k. For all tests, nev and nex are fixed to 2250 and 750. Only a single iteration of ChASE has been executed for all the experiments of weak scaling to ensure a fixed workload. This is because being an iterative method, ChASE might require different number of iterative steps for matrices with increasing size. 

Both the strong scaling behaviour of ChASE v1.2.1 and ChASE with/without NCCL  are tested.


## Data
The experiments require the generation of Uniform matrix of size 130k through the scripts in [matGen](../matGen) . The generated matrix should be avaiable in the folder [data](../../data).

## Software dependencies

### Build

The build of both CPU and GPU version ChASE requires

- a C/C++ compiler (GCC 11.3.0 tested)
- MPI (OpenMPI 4.1.4 tested)
- Intel MKL (version 2022.1.0 tested)
- CMake (version 3.23.1 tested)
- Boost (version 1.79.0 tested)
- git (version 2.36.0 tested)
- CUDA (version 11.7 tested): mandatory only for GPU build

### extract data

Extract of useful data from the output of experiments requires

- grep
- sed
- tr

### Plot

The plots of results require Python3 (version 3.8.5 tested) with the libraries:

- matplotlib (version 3.3.2 tested)
- pandas (version 1.3.2 tested)
- seaborn (version 0.11.0 tested)

## Structure

The structure of this folder is given as follows:

```bash
├── GPU
│   ├── v1.2
│   |	├── 1
│   |	|   ├── submit.sh
│   │ 	├── 4
│   |	|   ├── submit.sh
│   │ 	├── ...
│   │ 	├── 64
│   |	|   ├── submit.sh
│   ├── v1.3
│   |	├── 1
│   |	|   ├── submit.sh
│   │ 	├── 4
│   |	|   ├── submit.sh
│   │ 	├── ...
│   │ 	├── 64
│   |	|   ├── submit.sh
│   ├── v1.3-nccl
│   |	├── 1
│   |	|   ├── submit.sh
│   │ 	├── 4
│   |	|   ├── submit.sh
│   │ 	├── ...
│   │ 	├── 64
│   |	|   ├── submit.sh
│   ├── build_v12.sh
│   ├── build_v13.sh
│   ├── build_nccl.sh
│   ├── data.sh
│   ├── submit.sh
└── README.md
```

For the GPU build, it includes the folder `v1.2`, `v1.3` and `v1.3-nccl` for the job scripts of ChASE v1.2.1 and ChASE v1.3 without and with NCCL. For each version of build, it includes a series of folders `1`, `4`,`9`,..., which stores seperately for the slurm job script for 1, 4, 9 ... nodes. Additionally, the bash scripts `build_v12.sh`, `build_v13.sh` and `build_v13_nccl.sh` are available for different builds of ChASE.

The bash scripts for building ChASE, submitting slurm jobs and post data cleaning are available within [GPU](GPU).


## workflow

### GPU build and experiments

1. go into the folder [GPU](GPU)

```bash
cd GPU
```

2. build ChASE v1.2.1

```bash
./build_v12.sh
```

3. build ChASE v1.3.1 without NCCL

```bash
./build_v13.sh
```

4. build ChASE v1.3.1 with NCCL

```bash
./build_v13_nccl.sh
```

5. launch slurm jobs

For launching slurm jobs, it is required to provide a list of node numbers, which can be a subset of `1`,`4`,`9`, `16`,....

Below is an example to submit the jobs with node number 1, 4, 16.

```bash
./submit.sh 1,4,16
```

### extract data into CSV files

#### GPU build

in the folder [GPU](GPU):

```bash
./data.sh
```

### Plots

All the Python based plot scripts are available in the folder [plots](../../plots).
Plots for comparing the numerical behaviour of ChASE with houshoulder QR and with Cholesky QR can be accomplished by

```bash
python weak_scaling.py
```

**The Python plot script works even with a subset of points (node numbers)**.
