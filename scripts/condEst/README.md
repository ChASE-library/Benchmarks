# Estimating condition number

## Summary

ChASE introduced an estimation of condition number for the vectors filtered by Chebyshev polynomial. Based on this estimation, variants of QR implementation can be switch on the fly for each iteration to achieve good parallel performance and maintain the numerical stability.

The test problems used in this section are the real ones from DFT and BSE simulations. 
We carried on the tests with the polynomial degree optimization turned either on (OPT)) or off (NO-OPT) to show how the condition number estimation intrinsically depends on the optimization mechanism. 

For the case NO-OPT, the degree of Chebyshev polynomial is fixed to 20 at every iteration. For the case OPT, the initial degree for the first iteration is set as 20 and changes at every later iteration for each of the filtered vectors. A maximal allowed degree is fixed to $36$ to avoid the matrix of vectors becoming extremely ill-conditioned.

The estimations of condition number for each step are compared with the real condition number which has been computed by a LAPACK SVD solver.

All the experiments are performed with GPU build of ChASE on JUWELS-Booster.


## Data

The experiments require downloading the DFT and BSE matrices at first. Then an environment variable `DATA_PATH` should be set to the path to store the downloaded matrices.

## Software dependencies

### Build

The build of ChASE for these experiments require:

- a C/C++ compiler (GCC 11.3.0 tested)
- MPI (OpenMPI 4.1.4 tested)
- Intel MKL (version 2022.1.0 tested)
- CMake (version 3.23.1 tested)
- Boost (version 1.79.0 tested)
- git (version 2.36.0 tested)
- CUDA (version 11.7 tested)

### extract data

Extract of useful data from the output of experiments requires

- grep
- sed
- tr

### Plots

The plots of results require Python3 (version 3.8.5 tested) with the libraries:

- matplotlib (version 3.3.2 tested)
- pandas (version 1.3.2 tested)

## Structure

```bash
├── AuAg-13k
│   ├── OptN.sh
|   ├── Opt.sh
├── NaCl-9k
│   ├── OptN.sh
|   ├── Opt.sh
├── TiO2-29k
│   ├── OptN.sh
|   ├── Opt.sh
├── HfO2-76k
│   ├── OptN.sh
|   ├── Opt.sh
├── In2O3-76k
│   ├── OptN.sh
|   ├── Opt.sh
├── In2O3-115k
│   ├── OptN.sh
|   ├── Opt.sh
├── build.sh
├── submit.sh
├── data.sh
└── README.md
```

The folder `AuAg-13k`, `NaCl-9k`, `TiO2-29k`, `HfO2-76k`, `In2O3-76k` and `In2O3-115k` contain respectively the job scripts for each matrix. For example, in the folder `AuAg-13k`, there are two slurm job scripts: `OptN.sh` and `Opt.sh` which represent the job scripts for ChASE without and with degree optimization.

The bash script `build.sh` is to build ChASE for these experiments. The bash script `submit.sh` is to lanuch all slurm jobs. The required data are extracted by `data.sh` from output files and stored into a series of CSV files in `../../results`.

## Workflow

### Set the data path

Set the path where the downloaded matrices are stored:

```bash
export DATA_PATH=/path/store/DFT/Matrices
```

### GPU build and experiments

1. build ChASE with GPU support

```bash
./build.sh
```

2. lanuch all slurm jobs

```bash
./submit.sh
```

### extract data into CSV files

In the folder `condEst`:

```bash
./data.sh
```

### Plots

All the Python based plot scripts are available in the folder `../../plots`.

Plots for condition number estimation can be accomplished by

```bash 
python conEst.py
```




