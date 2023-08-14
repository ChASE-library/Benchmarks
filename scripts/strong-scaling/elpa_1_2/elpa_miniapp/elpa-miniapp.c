#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>
#include <math.h>

#include <elpa/elpa.h>
#include <assert.h>

#define assert_elpa_ok(x) assert(x == ELPA_OK)

const int i_zero = 0, i_one = 1;

#define EV_TYPE double
#define C_INT_TYPE long int

#define MAT_TYPE complex double
char SCALAR[] = "complex double";


void Numroc(C_INT_TYPE n, C_INT_TYPE nb, int iproc, int isrcproc, int nprocs, C_INT_TYPE *n_loc, C_INT_TYPE *blocknb){

    C_INT_TYPE numroc;
    C_INT_TYPE extrablks, mydist, nblocks;
    mydist = (nprocs + iproc - isrcproc) % nprocs;
    nblocks = n / nb;
    numroc = (nblocks / nprocs) * nb;
    extrablks = nblocks % nprocs;

    if(mydist < extrablks)
        numroc = numroc + nb;
    else if(mydist == extrablks)
        numroc = numroc + n % nb;

    int nb_loc = numroc / nb;

    if(numroc % nb != 0){
        nb_loc += 1;
    }

    *n_loc = numroc;
    *blocknb = nb_loc;
}


void readMatrix(MAT_TYPE *H, char * path_in, C_INT_TYPE size, C_INT_TYPE m, C_INT_TYPE mblocks, C_INT_TYPE nblocks, 
				C_INT_TYPE *r_offs, C_INT_TYPE *r_lens, C_INT_TYPE *r_offs_l,
				C_INT_TYPE *c_offs, C_INT_TYPE *c_lens, C_INT_TYPE *c_offs_l)
{
    C_INT_TYPE N = size;
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0) printf("reading matrix %s...\n", path_in);

    FILE* fd;
    fd = fopen(path_in,"rb");

    for(C_INT_TYPE j = 0; j < nblocks; j++){
	for(C_INT_TYPE i = 0; i < mblocks; i++){
	    for(C_INT_TYPE q = 0; q < c_lens[j]; q++){
		fseek(fd, ((q + c_offs[j]) * N + r_offs[i])* sizeof(MAT_TYPE), SEEK_SET);
		fread(&H[(q + c_offs_l[j]) * m + r_offs_l[i]], sizeof(MAT_TYPE), r_lens[i], fd);
	    }
	}
    }

    if (rank == 0) printf("matrix loaded ...\n");

    fclose(fd);

}

int main(int argc, char** argv) {

    MPI_Init(&argc, &argv);

    int myid, nprocs;
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);
    MPI_Comm_size(MPI_COMM_WORLD, &nprocs);

    int np_cols, np_rows;

    for (np_cols = (int)sqrt((double) nprocs); np_cols > 1; np_cols--) {
        if (nprocs % np_cols == 0) {
            break;
        }
    }

    np_rows = nprocs/np_cols;

    //Setup 2D grid of MPI procs
    int periodic[] = {0, 0};
    int reorder = 0;
    int free_coords[2];
    int dims_[2];
    int tmp_dims_[2];
    int tmp_coord_[2];
    int coord_[2];
    MPI_Comm cartComm, row_comm_, col_comm_;
    // create cartesian communicator
    dims_[1] = np_cols; dims_[0] = np_rows;
    tmp_dims_[0] = np_cols; tmp_dims_[1] = np_rows;
    MPI_Cart_create(MPI_COMM_WORLD, 2, tmp_dims_, periodic, reorder, &cartComm);
    MPI_Comm_size(cartComm, &nprocs);
    MPI_Comm_rank(cartComm, &myid);
    MPI_Cart_coords(cartComm, myid, 2, tmp_coord_);
    coord_[1] = tmp_coord_[0];
    coord_[0] = tmp_coord_[1];

    // row communicator
    free_coords[0] = 1;
    free_coords[1] = 0;
    MPI_Cart_sub(cartComm, free_coords, &row_comm_);

    // column communicator
    free_coords[0] = 0;
    free_coords[1] = 1;
    MPI_Cart_sub(cartComm, free_coords, &col_comm_);

    int my_prow, my_pcol;
    my_prow = coord_[0];
    my_pcol = coord_[1];
   
    int row_procs, col_procs;
    MPI_Comm_size(row_comm_, &row_procs);
    MPI_Comm_size(col_comm_, &col_procs);

    //parser the arguments from command line
    C_INT_TYPE na ; //lobal dimension of the matrix to be solved
    C_INT_TYPE nblk ; //the block size of the scalapack block cyclic distribution
    C_INT_TYPE nev ; // number of eigenvectors to be computed
    int info;
    char *filename;

    //parse the arguments
    if (argc == 5) {
        na = atoi(argv[1]);
        nev = atoi(argv[2]);
        nblk = atoi(argv[3]);
	filename = argv[4];
    } else {
        na = 12455;
        nev = 1076;
        nblk = 16;
	filename = "/p/project/cslai/slai00/MATrix/TiO2/size12k/bin/gmat\ \ 1\ \ 1.bin";
    }


    C_INT_TYPE na_rows, na_cols, rblks, cblks;
   
    Numroc( na, nblk, my_prow, i_zero, dims_[0], &na_rows, &rblks );
    Numroc( na, nblk, my_pcol, i_zero, dims_[1], &na_cols, &cblks );

#if defined(TEST_OUTPUT)    
    //Output the information about 2D grid and block-cyclic distribution
    printf("Block-cyclic Distribution]> grid dims: %dx%d, myrank: %d, mycoord: (%d, %d), row_comm_size: %d, col_comm_size: %d, local matrix size: %dx%d\n", dims_[0], dims_[1], myid, my_prow, my_pcol, row_procs, col_procs, na_rows, na_cols);
#endif

    //Allocate matrices
    MAT_TYPE *a = malloc(na_rows * na_cols * sizeof(MAT_TYPE));
    EV_TYPE *ev = malloc(na * sizeof(EV_TYPE));
    MAT_TYPE *z = malloc(na_rows * na_cols * sizeof(MAT_TYPE));

    //MPI IO for loading matrix from local
    //char *filename = "NaCl_gmat_1_1.bin";

    C_INT_TYPE *r_offs_ = malloc(rblks * sizeof(C_INT_TYPE));
    C_INT_TYPE *r_lens_ = malloc(rblks * sizeof(C_INT_TYPE));
    C_INT_TYPE *r_offs_l_ = malloc(rblks * sizeof(C_INT_TYPE));
    C_INT_TYPE *c_offs_ = malloc(cblks * sizeof(C_INT_TYPE));
    C_INT_TYPE *c_lens_ = malloc(cblks * sizeof(C_INT_TYPE));
    C_INT_TYPE *c_offs_l_ = malloc(cblks * sizeof(C_INT_TYPE));

    C_INT_TYPE sendr = 0;
    C_INT_TYPE sendc = 0;
    C_INT_TYPE cnt = 0;
    C_INT_TYPE nr, nc;

    for(C_INT_TYPE r = 0; r < na; r += nblk, sendr = (sendr + 1) % dims_[0]){
        nr = nblk;
        if (na - r < nblk){
            nr = na - r;
        }

       if(coord_[0] == sendr){
           r_offs_[cnt] = r;
           r_lens_[cnt] = nr;
           cnt++;
       }
    }


    cnt = 0;
    for(C_INT_TYPE c = 0; c < na; c += nblk, sendc = (sendc + 1) % dims_[1]){
	nc = nblk;
	if(na - c < nblk){
	   nc = na - c;
	}
	if(coord_[1] == sendc){
           c_offs_[cnt] = c;
           c_lens_[cnt] = nc;
	   cnt++;	
	}	    
    }	

    r_offs_l_[0] = 0;
    c_offs_l_[0] = 0;

    for(C_INT_TYPE i = 1; i < rblks; i++){
       r_offs_l_[i] = r_offs_l_[i - 1] + r_lens_[i - 1];
    }

    for(C_INT_TYPE j = 1; j < cblks; j++){
       c_offs_l_[j] = c_offs_l_[j - 1] + c_lens_[j - 1];
    } 

    readMatrix(a, filename, na, na_rows, rblks, cblks, r_offs_, r_lens_, r_offs_l_, c_offs_, c_lens_, c_offs_l_);

    elpa_init(20221109);

    elpa_t handle;
    int error_elpa, value;
    handle = elpa_allocate(&error_elpa);

    /* Set parameters */
    elpa_set(handle, "na", (int) na, &error_elpa);
    assert_elpa_ok(error_elpa);

    elpa_set(handle, "nev", (int) nev, &error_elpa);
    assert_elpa_ok(error_elpa);
    
    elpa_set(handle, "local_nrows", (int) na_rows, &error_elpa);
    assert_elpa_ok(error_elpa);
  
    elpa_set(handle, "local_ncols", (int) na_cols, &error_elpa);
    assert_elpa_ok(error_elpa);
 
    elpa_set(handle, "nblk", (int) nblk, &error_elpa);
    assert_elpa_ok(error_elpa);
  
    elpa_set(handle, "mpi_comm_parent", (int)(MPI_Comm_c2f(MPI_COMM_WORLD)), &error_elpa);

    assert_elpa_ok(error_elpa);
    
    elpa_set(handle, "process_row", (int) my_prow, &error_elpa);
    assert_elpa_ok(error_elpa);

    elpa_set(handle, "process_col", (int) my_pcol, &error_elpa);
    assert_elpa_ok(error_elpa);

    /* Setup */    
    assert_elpa_ok(elpa_setup(handle));
    
    int elpa_solver=2;
    char* elpa_solver_env;
    elpa_solver_env = getenv("ELPA_MINIAPPS_SOLVER");
    if (elpa_solver_env)
    {
        elpa_solver = atoi(elpa_solver_env);
    }

    /* Set tunables */
    if(elpa_solver == 1){
        elpa_set(handle, "solver", ELPA_SOLVER_1STAGE, &error_elpa);
    }else{
        elpa_set(handle, "solver", ELPA_SOLVER_2STAGE, &error_elpa);
    }

    assert_elpa_ok(error_elpa);
     
    elpa_set(handle, "nvidia-gpu", 1, &error_elpa);
    assert_elpa_ok(error_elpa);

    if(elpa_solver == 2){
        elpa_set(handle, "complex_kernel", ELPA_2STAGE_COMPLEX_NVIDIA_GPU, &error_elpa);
        assert_elpa_ok(error_elpa);
    }

    elpa_get(handle, "solver", &value, &error_elpa);
    
    // Solve EV problem 
    double start, end;
    start = MPI_Wtime(); 
    elpa_eigenvectors(handle, a, ev, z, &error_elpa);
    assert_elpa_ok(error_elpa);
    end = MPI_Wtime();

    if (myid == 0) {
	printf("->Solver %d: %d,%d,%f\n",elpa_solver,nprocs,nev,end-start);
    }

    MPI_Barrier(MPI_COMM_WORLD);

    if(myid == 0){
    	printf("Finished Problem\n");
    	printf("Printing first %d eigenvalues and residuals\n", 10);
    	printf("Index : Eigenvalues\n");
    	printf("----------------------\n");
    }

    for(C_INT_TYPE i = 0; i < 10; i++){
        if(myid == 0) printf("%d    : %.6e\n",i+1, ev[i]);
    }

    elpa_deallocate(handle, &error_elpa);
    elpa_uninit(&error_elpa);
    free(a);
    free(z);
    free(ev);

    MPI_Finalize();

}
