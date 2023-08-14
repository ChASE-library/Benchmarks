# SC23-Artifact

## Summary

The benchmarks of [ChASE eigensolver](https://github.com/ChASE-library/ChASE) was run on the supercomputer [JUWELS-Booster](https://apps.fz-juelich.de/jsc/hps/juwels/configuration.html) for the GPU build.

JUWELS-Booster composes 936 NVIDIA GPU-accelerated compute nodes. The configuration of each node is two 24 cores AMD EPYC 7402 CPUs @ 2.25 GHz (16x32 GB DDR4 Memory), 4xNVIDIA A100 GPU with 40 GB memory. The interconnect are 4x InfiniBand HDR (Connect-X6).

The bencmarks include the numerical tests:

- validation of our proposed condition number estimation vs real condition number computed by SVD
- Comparison of numerical behaviors of ChASE with Householder QR and with a flexible selection of communication-avoiding variants of CholeskyQR based on the estimation of condition numbers of filtered vectors

and the parallel performance tests:

- communication, computation and data movement costs in the kernels **Filter**, **QR**, **Rayleigh-Ritz** and **Residuals**
- overhead of initialization
- weak scaling for the GPU builds, and its comparison with previous version
- strong scaling for the GPU builds, and its comparison with previous version and [ELPA](https://elpa.mpcdf.mpg.de/) eigensolver library

We provide a collection of artificats:

- ChASE software: https://github.com/ChASE-library/ChASE
- DEMAGIS software for artificial matrix generation with given spectrum: https://github.com/SimLabQuantumMaterials/DEMAGIS
- DFT and BSE matrices for numerical tests: https://doi.org/10.26165/JUELICH-DATA/OFQWGZ
- scripts files for the software builds, job submissions (SLURM based), data extraction from output files and visualization of final results: https://github.com/ChASE-library/Benchmarks.git

With all the artifcats provided, the results are fully reproducible. For the strong and weak scaling tests, it is not necessary to run all the points, and the data extraction and visualization scripts can still produce a meaningful results closed to the one in the paper.

## Software dependencies

The build of both CPU and GPU version ChASE requires

- a C/C++ compiler (GCC 11.3.0 tested)
- MPI (OpenMPI 4.1.4 tested)
- Intel MKL (version 2022.1.0 tested)
- CMake (version 3.23.1 tested)
- Boost (version 1.79.0 tested)
- CUDA (version 11.7 tested)
- git (version 2.36.0 tested)

ChASE is able to be built on top of any BLAS, LAPACK, ScaLAPACK variants, but the ones we use are Intel MKL.

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


## Quick build of ChASE

The builds of ChASE on multiple platforms and Operating systems are available in the [Documentation](https://chase-library.github.io).

All the benchmarks uses the **/examples/2_input_output** in the ChASE repository, a detailed explanation of this example is available in this [link](https://chase-library.github.io/ChASE/example.html#parallel-i-o-and-configuration).

This example relies on Boost for parsing command line arguments, and we list some important options of **/examples/2_input_output**  as follows

```bash
ChASE Options:
  -h [ --help ]           show this message
  --n arg                 Size of the Input Matrix
  --double arg (=1)       Is matrix double valued, false indicates the single
                          type
  --complex arg (=1)      Matrix is complex, false indicated the real matrix
  --nev arg               Wanted Number of Eigenpairs
  --nex arg (=25)         Extra Search Dimensions
  --deg arg (=20)         Initial filtering degree
  --maxDeg arg (=36)      Sets the maximum value of the degree of the Chebyshev
                          filter
  --maxIter arg (=25)     Sets the value of the maximum number of subspace
                          iterationswithin ChASE
  --tol arg (=1e-10)      Tolerance for Eigenpair convergence
  --path_in arg           Path to the input matrix/matrices
  --mode arg (=A)         valid values are R(andom) or A(pproximate)
  --opt arg (=S)          Optimi(S)e degree, or do (N)ot optimise
  --lanczosIter arg (=25) Sets the number of Lanczos iterations executed by
                          ChASE.
  --numLanczos arg (=4)    Sets the number of stochastic vectors used for the
                          spectral estimatesin Lanczos
```

## Workflow of experiments

**We want to clarify that all the builds and SLRUM jobs for the benchmarks are provided [here](https://github.com/ChASE-library/Benchmarks.git)**. It is not necessary to build ChASE by hand. 

For the benchmark, it is enough to clone this repository as follows:

```bash
git clone https://github.com/ChASE-library/Benchmarks.git
```

There are 4 folders inside:

- [scripts](scripts): this folder contains all the required SLURM job scripts, data extraction scripts for all benchmarks.
- [plots](plots): this folder contains the python scripts for the visualization of the results of all benchmarks.
- [results](results):  this folder is designed to store the results of all benchmarks in CSV format.
- [data](data): this folder is designed to store the generated artificial matrices.

### Artifical matrix generation

1. Scripts: [scripts/matGen](scripts/matGen)
2. Instructions: [scripts/matGen/README.md](scripts/matGen/README.md).

### Estimating the condition number

1. Scripts: [scripts/condEst](scripts/condEst)
2. Instructions: [scripts/condEst/README.md](scripts/condEst/README.md).


### ChASE with CholeskyQR vs with HHQR

1. Scripts: [scripts/hhQR_vs_cholQR](scripts/hhQR_vs_cholQR)
2. Instructions: [scripts/hhQR_vs_cholQR/README.md](scripts/hhQR_vs_cholQR/README.md).

### Communication, Computation and data movement overheads

1. Scripts: [scripts/commVScompute](scripts/commVScompute)
2. Instructions: [scripts/commVScompute/README.md](scripts/commVScompute/README.md).

### Weak scaling

1. Scripts: [scripts/weak-scaling](scripts/weak-scaling)
2. Instructions: [scripts/weak-scaling/README.md](scripts/weak-scaling/README.md).

### Strong scaling

1. Scripts: [scripts/strong-scaling](scripts/strong-scaling)
2. Instructions: [scripts/strong-scaling/README.md](scripts/strong-scaling/README.md).







