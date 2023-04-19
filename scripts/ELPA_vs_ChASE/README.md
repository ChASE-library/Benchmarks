# ELPA vs ChASE

## Summary

We compare ChASE with [ELPA](https://elpa.mpcdf.mpg.de/), the state-of-the-art eigensolver for solving dense Hermitian eigenproblems on both distributed-memory homogeneous and heterogeneous systems. A strong scaling test up to 256 compute nodes have been performed on JUWELS-Booster to compare ChASE-GPU with both ELPA1 and ELPA2 with GPU support. The same strong scaling test is also performed for ChASE-CPU on JURECA-DC up to 256 nodes.

The eigenproblem that we use for this test is In2O3 115k. For both ChASE and ELPA the number of eigenpairs sought after is set at 1200, representing ~1% of the full spectrum. For ChASE, the size of the external searching space {\sf nex} is fixed as 400. 

## Data
The expriements require downloading the DFT and BSE matrices at first. Then an environment variable `DATA_PATH` should be set to the path to store the downloaded matrices.

## Software dependencies

### Build

The build of both CPU and GPU version ChASE requires

- a C/C++ compiler (GCC 11.2.0 tested)
- MPI (OpenMPI 4.1.2 tested)
- Intel MKL (version 2021.4.0 tested)
- CMake (version 3.21.1 tested)
- Boost (version 1.78.0 tested)
- git (version 2.33.0 tested)
- CUDA (version 11.5 tested): mandatory only for GPU build

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
- numpy (version 1.19.2 tested)

## Structure

The structure of this folder is given as follows:

```bash
├── chase
│   ├── CPU
│   |	├── 4
│   |	|   ├── submit.sh
│   │ 	├── 8
│   |	|   ├── submit.sh
│   │ 	├── ...
│   │ 	├── 256
│   |	|   ├── submit.sh
│   ├── GPU
│   |	├── 4
│   |	|   ├── submit.sh
│   │ 	├── 8
│   |	|   ├── submit.sh
│   │ 	├── ...
│   │ 	├── 256
│   |	|   ├── submit.sh
│   ├── build.sh
│   ├── data.sh
│   ├── submit.sh
├── elpa_1_2
│   ├── elpa_miniapp
│   ├── 4
│   |   ├── submit.sh
│   ├── 8
│   |   ├── submit.sh
│   ├── ...
│   ├── 256
│   |   ├── submit.sh
│   ├── build.sh
│   ├── data.sh
│   ├── submit.sh
└── README.md
```

This folder includes two sub-folders `chase` and `elpa_1_2`. As shown by their names, `chase` contains the script files for both CPU and GPU builds of ChASE-v1.3.1. For both CPU and GPU builds of ChASE, the script files include the slurm job files for different number of compute nodes, and the scripts for building, submitting jobs and extracting data from output files.

For `elpa_1_2`, there is a folder `elpa_miniapp`, which is an implementation of test app for solving a standard eigenproblem by ELPA. It is used for the benchmark of ELPA1 and ELPA2. The script file `build.sh` is to build ELPA with GPU support. The version of ELPA is selected as `new_release_2022.11.001.rc1`. The scripts for submitting jobs and extracting data from output files are also avaiable in this folder.


## workflow

### Set the data path

Set the path where the downloaded matrices are stored:

```bash
export DATA_PATH=/path/store/DFT/Matrices
```


### ChASE CPU build and experiments

1. go into the folder `chase/CPU`

```bash
cd chase/CPU
```

2. build ChASE v1.3.1

```bash
./build.sh
```

4. launch slurm jobs

For launching slurm jobs, it is required to provide a list of node numbers, which can be a subset of `4`,`8`,`16`, `32`,...`256`.

Below is an example to submit the jobs with node number 4, 16.

```bash
./submit.sh 4,16
```
### ChASE GPU build and experiments

1. go into the folder `chase/GPU`

```bash
cd chase/GPU
```

2. build ChASE v1.3.1

```bash
./build.sh
```

4. launch slurm jobs

For launching slurm jobs, it is required to provide a list of node numbers, which can be a subset of `4`,`8`,`16`, `32`,...`256`.

Below is an example to submit the jobs with node number 4, 16.

```bash
./submit.sh 4,16
```

### ELPA GPU build and experiments

1. go into the folder `elpa_1_2`

```bash
cd elpa_1_2
```

2. build ELPA

```bash
./build.sh
```

4. launch slurm jobs

For launching slurm jobs, it is required to provide a list of node numbers, which can be a subset of `4`,`8`,`16`, `32`,...`256`.

Below is an example to submit the jobs with node number 4, 16.

```bash
./submit.sh 4,16
```
**For each job, both ELPA1 and ELPA2 solvers are tested**. 

### extract data into CSV files

#### ChASE CPU build

in the folder `chase/CPU`:

```bash
./data.sh
```

#### ChASE GPU build

in the folder `chase/GPU`:

```bash
./data.sh
```

#### ELPA GPU build

in the folder `elpa_1_2`:

```bash
./data.sh
```

### Plots

All the Python based plot scripts are available in the folder `../../plots`.
Plots for comparing ChASE with ELPA can be done as

```bash
python chase_vs_elpa.py
```

**The Python plot script works even with a subset of points (node numbers)**.
