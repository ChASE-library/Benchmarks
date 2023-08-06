# ChASE with Househoulder QR and CholeksyQR

## Summary

The experiments are designed to compare the numerical behavior of ChASE equipped with Househoulder QR (HHQR) (for all ChASE iterations) with the automatic selection of QR variants based on the heuristic with condition number estimation of Cheyshev polynomial vectors for each iteration. HHQR specifically refers to the Householder QR implementation provided by ScaLAPACK, which uses a 1D MPI grid and is executed independently over each column communicator. The block size of ScaLAPACK block-cyclic distribution for the rows is the same as the number of rows of $C$, and the block size for the columns is fixed at 32.

The test problems used in this section are the real ones from DFT and BSE simulations. ChASE with GPU build is tested using $4$ compute nodes on JUWELS-Booster.

## Data

The experiments require downloading the DFT and BSE matrices at first. Then an environment variable `DATA_PATH` should be set to the path to store the downloaded matrices.

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
- cut

### Plot

The plots of results require `Python3` (version 3.8.5 tested) with the libraries:

- matplotlib (version 3.3.2 tested)
- pandas (version 1.3.2 tested)

## Structure

The structure of this folder is given as follows:

```bash
├── GPU
│   ├── AuAg-13k
│   |	├── cholQR.sh
│   │ 	├── hhQR.sh
│   ├── NaCl-9k
│   |	├── cholQR.sh
│   │ 	├── hhQR.sh
│   ├── TiO2-29k
│   |	├── cholQR.sh
│   │ 	├── hhQR.sh
|   ├── HfO2-76k
|   │   ├── OptN.sh
|   |   ├── Opt.sh
|   ├── In2O3-76k
|   │   ├── OptN.sh
|   |   ├── Opt.sh
|   ├── In2O3-115k
|   │   ├── OptN.sh
|   |   ├── Opt.sh
│   ├── build.sh
│   ├── data.sh
│   ├── submit.sh
└── README.md
```

For the GPU build, it includes the slurm job scripts for each test problem, which are saved separately in the folder `AuAg-13k`, `NaCl-9k`, and `TiO2-29k`...

For each test problem, there are two slurm job scripts: `cholQR.sh` and `hhQR.sh`, which represents the ones for ChASE with CholeksyQR and ChASE with only ScaLAPACK QR.

The bash scripts for building ChASE, submitting slurm jobs and post data cleaning are available.

## workflow

### Set the data path

Set the path where the downloaded matrices are stored:

```bash
export DATA_PATH=/path/store/DFT/Matrices
```

### GPU build and experiments

1. go into the folder `GPU`

```bash
cd GPU
```

2. build ChASE

```bash
./build.sh
```

3. launch all slurm jobs

```bash
./submit.sh
```

### extract data into CSV files

#### GPU build

in the folder `GPU`:

```bash
./data.sh
```

### Plots

All the Python based plot scripts are available in the folder `../../plots`.
Plots for comparing the numerical behaviour of ChASE with houshoulder QR and with Cholesky QR can be accomplished by

```bash
python hhQR_vs_CholQR.py
```
