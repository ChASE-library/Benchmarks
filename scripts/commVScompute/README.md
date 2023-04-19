# Communication vs Computation

## Summary

These experiments compare communication vs computation of kernels **QR**, **Rayleigh-Ritz** and **Residuals**, and the initialization overheads for both ChASE v1.2.1 and v1.3.1. We designed a weak-scaling experiment, in which the count of compute nodes increases from 1 to 64, while the matrix size increases from 30k to 240k.  Only the first iteration is reported, which ensures a fixed workload with the increase of compute nodes count. The experiments are carried on JURECA-DC and JUWELS-Booster for ChASE-CPU and ChASE-GPU, respectively. For this experiment, we used artificial matrices of type Uniform with nev and nex being fixed to 2250 and 750.

The measurement of the timings of different kernels are effectued by inserting Nvidia [NVTX](https://docs.nvidia.com/nvtx/) event macros.
Therefore, CUDA is mandatory for both CPU and GPU builds.

## Data

The experiments require the generation of Uniform matrix of size 30k, 60k, 120k and 240k through the scripts in [matGen](../matGen) . The generated matrix should be avaiable in the folder [data](../../data).

## Software dependencies

### Build

The build of both CPU and GPU version ChASE requires

- a C/C++ compiler (GCC 11.2.0 tested)
- MPI (OpenMPI 4.1.2 tested)
- Intel MKL (version 2021.4.0 tested)
- CMake (version 3.21.1 tested)
- Boost (version 1.78.0 tested)
- git (version 2.33.0 tested)
- CUDA (version 11.5 tested)

CUDA is mandatory for both CPU and GPU builds since we use NVTX events to record the communication and computation timings.

### extract data

Extract of useful data from the output of profiling requires 

- `sqlite3` (version 3.35.5 tested)
	
to query the database.

### Plot

The plots of results require `Python3` (version 3.8.5 tested) with the libraries:

- matplotlib (version 3.3.2 tested)
- pandas (version 1.3.2 tested)

## Structure

The structure of this folder is given as follows:

```bash
├── ChASE-v1.2
├── CPU
│   ├── v1.2
│   |	├── 1
│   │ 	├── 4
│   │  	├── 16
│   │  	|── 64
|   ├── v1.3
│   |	├── 1
│   |	├── 4
│   |	├── 16
│   |   |── 64
|   ├── build_v12.sh
|   ├── build_v13.sh
|   ├── submit.sh
├── GPU
│   ├── v1.2
│   |	├── 1
│   |	├── 4
│   |	├── 16
│   |	|── 64
|   ├── v1.3
│   |	├── 1
│   |	├── 4
│   |	├── 16
│   |   |── 64
|   ├── build_v12.sh
|   ├── build_v13.sh
|   ├── submit.sh
├── query_init_v13.sh
├── query_init_v12.sh
├── query_v12.sh
├── query_v13.sh
├── write.sh
└── README.md
```
In the directory `ChASE-v1.2`, a simplified version of ChASE v1.2.1 is provided by inserting the required NVTX macros. The reason to provide this simplified version is that NVTX marcos are not available in the release version v1.2.1.

The scripts for CPU and GPU builds are available in two seperate folders `CPU` and `GPU`. Here, we use the CPU build as an example to explain the structure. There are two bash scripts `build_v12.sh` and `build_v13.sh`, which is to build ChASE v1.2.1 and v1.3.1 in this folder.
The folders `1`, `4`, `16`, `64` contain the script for the experiments with 1, 4, 16, 64 nodes on JURECA-DC, respectively. Finally, the bash script `submit.sh` is used to submit all the jobs in this `CPU` folder. 

The output for each case is stored in its own folder, and the NVTX records are stored in a SQLite database named as `report1.sqlite`. The communication and computation costs are extracted through the querys of `sqlite3`, and the the querys are stored in the scripts `query_v12.sh` and `query_v13.sh` for ChASE v1.2.1 and v1.3.1. For the overheads of initialization, the querys are available in the scripts `query_init_v12.sh` and `query_init_v13.sh`. The script `write.sh` is to write the queried results into CSV files.


## Workflow

### CPU build and experiments

1. go into the folder `CPU`

```bash
cd CPU
```

2. build ChASEv1.2.1

```bash
./build_v12.sh
```

3. build ChASEv1.3.1

```bash
./build_v13.sh
```

4. submit jobs

```bash
./submit.sh
```

### GPU build and experiments

1. go into the folder `GPU`

```bash
cd GPU
```

2. build ChASEv1.2.1

```bash
./build_v12.sh
```

3. build ChASEv1.3.1

```bash
./build_v13.sh
```

4. submit jobs

```bash
./submit.sh
```

### extract data into CSV file

In the folder `commVScompute`

```bash
./write.sh
```

The results of communication vs computation will be saved as `../../results/chase_Kernel_comm_vs_compute.csv`

The results of initialization overheads will be saved as `../../results/Initialization_overhead_old.csv` and `../../results/Initialization_overhead_new.csv` for ChASE v1.2.1 and v1.3.1, respectively.

### Plot

All the Python based plot scripts are available in the folder [plots](../../plots).

### Plots for communication vs compuation

```bash
python comm_vs_compt.py
```

The plots, `QR-CPU.jpeg`, `QR-GPU.jpeg`, `RR-CPU.jpeg`, `RR-GPU.jpeg`, `Resid-CPU.jpeg`, `Resid-GPU.jpeg` are available in the folder `../../plots/jpeg`. 



### Plots for the initialization overheads

```bash
python Init.py
```

The plots, `Init-old-ChASE.jpeg` and `Init-new-ChASE.jpeg` are available in the folder [plots/jpeg](../../plots/jpeg), which correspond respectively to ChASE v1.2.1 and v1.3.1.
