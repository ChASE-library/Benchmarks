# Generation of artifical matrices

## Summary

This sub-project is to generate the artificial matrices for the benchmark of parallel performance of ChASE. The generation is inspired by the testing infrastructure for symmetric tridiagonal eigensolvers of LAPACK. To generate them, we construct a diagonal matrix $D$ whose diagonal is filled by the prescribed eigenvalues. Then a dense matrix $A$ with the given spectra is generated as $A=Q^TDQ$, with $Q$ the Q factor of the QR factorization of a randomly generated square matrix. In this paper, the eigenvalues of the artificial matrices are distributed uniformly within the $(0, d_{max}\epsilon]$ interval and will be referred to as Uniform matrices.
 

## Data

----


## Software dependencies

### Build

The build of both CPU and GPU version ChASE requires

- a C/C++ compiler (GCC 11.3.0 tested)
- MPI (OpenMPI 4.1.4 tested)
- Intel MKL (version 2022.1.0 tested)
- CMake (version 3.23.1 tested)
- Boost (version 1.79.0 tested)
- git (version 2.36.0 tested)

## Structure

The structure of this folder is given as follows:

```bash
├── 30k
├──  ├── matgen.sh 
├── 60k
├──  ├── matgen.sh 
├── 90k
├──  ├── matgen.sh 
├── 120k
├──  ├── matgen.sh 
├── 150k
├──  ├── matgen.sh 
├── ...
├── 600k
├──  ├── matgen.sh 
├── 750k
├──  ├── matgen.sh 
├── 900k
├──  ├── matgen.sh 
│── build.sh
│── submit.sh
└── README.md
```

The script `build.sh` is to build [DEMAGIS](https://github.com/SimLabQuantumMaterials/DEMAGIS) for the generation of matrices. The script `submit.sh` is to submit the slurm jobs.

Each folder of `30k`, `60k`, `90k` ... contains a slurm job script file `matgen.sh`.

All the matrices of different sizes are for the weak scaling tests of ChASE.

## workflow

### build and generation

1. build DEMAGIS

```bash
./build.sh
```

2. launch slurm jobs

For launching slurm jobs, it is required to provide a list of matrix sizes, which can be a subset of `30k`,`60k`,`90k`, `120k`,...`900k`.

Below is an example to submit the jobs with matrices `30k`,`60k`,`90k`, `150k`

```bash
./submit.sh 30k,60k,90,150k
```

All the matrices are saved in the folder [data](../../data). 
