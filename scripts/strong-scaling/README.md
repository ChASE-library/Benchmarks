# Strong scaling

## Summary

The strong scaling experiments of ChASE-CPU and ChASE-GPU are done using an artifical matrix of size 130,000. nev and nex are fixed as 1000 and 300 respectively. The compute nodes count are selected to be square of integers $1, 4, 9, \cdots, 64$.

Both the strong scaling behaviour of ChASE v1.2.1 and ChASE v1.3.1 are tested.

## Data
The experiments require the generation of Uniform matrix of size 130k through the scripts in [matGen](../matGen) . The generated matrix should be avaiable in the folder [data](../../data).

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

## Structure

The structure of this folder is given as follows:

```bash
├── CPU
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
│   ├── build_v12.sh
│   ├── build_v13.sh
│   ├── data.sh
│   ├── submit.sh
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
│   ├── build_v12.sh
│   ├── build_v13.sh
│   ├── data.sh
│   ├── submit.sh
└── README.md
```

The CPU and GPU builds and experiments are saved in two seperated folders [CPU](CPU) and [GPU](GPU).
For each build, it includes the folder `v1.2` and `v1.3` for the job scripts of ChASE v1.2.1 and ChASE v1.3.1. For each version of build, it includes a series of folders `1`, `4`,`9`,...,`64`, which stores seperately for the slurm job script for 1, 4, 16 ... nodes. Additionaly, the bash scripts `build_v12.sh` and `build_v13.sh` are available, which are for the CPU build of ChASE v1.2.1 and ChASE v1.3.1.

The bash scripts for building ChASE, submitting slurm jobs and post data cleaning are available within [CPU](CPU) and [GPU](GPU).


## workflow

### CPU build and experiments

1. go into the folder [CPU](CPU)

```bash
cd CPU
```

2. build ChASE v1.2.1

```bash
./build_v12.sh
```

3. build ChASE v1.3.1

```bash
./build_v13.sh
```

4. launch slurm jobs

For launching slurm jobs, it is required to provide a list of node numbers, which can be a subset of `1`,`4`,`9`, `16`,...`64`.

Below is an example to submit the jobs with node number 1, 4, 16.

```bash
./submit.sh 1,4,16
```
### GPU build and experiments

1. go into the folder [GPU](GPU)

```bash
cd GPU
```

2. build ChASE v1.2.1

```bash
./build_v12.sh
```

3. build ChASE v1.3.1

```bash
./build_v13.sh
```

4. launch slurm jobs

For launching slurm jobs, it is required to provide a list of node numbers, which can be a subset of `1`,`4`,`9`, `16`,...`64`.

Below is an example to submit the jobs with node number 1, 4, 16.

```bash
./submit.sh 1,4,16
```

### extract data into CSV files

#### CPU build

in the folder [CPU](CPU):

```bash
./data.sh
```

#### GPU build

in the folder [GPU](GPU):

```bash
./data.sh
```

### Plots

All the Python based plot scripts are available in the folder [plots](../../plots).
Plots for comparing the numerical behaviour of ChASE with houshoulder QR and with Cholesky QR can be accomplished by

```bash
python strong_scaling.py
```

**The Python plot script works even with a subset of points (node numbers)**.
