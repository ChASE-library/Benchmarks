import pandas as pd
import sys

def NCCL_data_retrieve(node, path):
	df = pd.read_csv(path, names=["Operations", "Times(s)"])

	### Filter ###
	filter_compute = df[['Times(s)']].where(df['Operations'] == '+ Filter/GEMM')
	filter_compute_sum = filter_compute.sum()/4 / node

	filter_comm = df[['Times(s)']].where(df['Operations'] == '+ Filter/AllReduce')
	filter_comm_sum = filter_comm.sum()/4/ node
	filter_copy_sum = 0.0

	### QR ###
	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/syherk')
	qr_compute_sum = qr_compute.sum() / 4/ node

	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/Potrf')
	qr_compute_sum += qr_compute.sum() / 4/ node

	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/Trsm')
	qr_compute_sum += qr_compute.sum() / 4/ node

	qr_comm = df[['Times(s)']].where(df['Operations'] == '+ QR/AllReduce')
	qr_comm_sum = qr_comm.sum() / 4/ node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/Memcpy')
	qr_copy_sum = qr_copy.sum() / 4/ node

	### RR ###
	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ RR/GEMM')
	rr_compute_sum = rr_compute.sum() / 4/ node

	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ RR/HEEVD')
	rr_compute_sum += rr_compute.sum() / 4/ node

	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/GEMM')
	rr_compute_sum += rr_compute.sum() / 4 / 2/ node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ RR/AllReduce')
	rr_comm_sum = rr_comm.sum() / 4/ node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/AllReduce')
	rr_comm_sum += rr_comm.sum() / 4 / 2/ node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/Bcast')
	rr_comm_sum += rr_comm.sum() / 4 / 2/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/D2H')
	rr_copy_sum = rr_copy.sum() / 4/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/H2D')
	rr_copy_sum += rr_copy.sum() / 4/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/Memcpy')
	rr_copy_sum += rr_copy.sum() / 4/ node

	### Residual ###
	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ Resd/Residual')
	resd_compute_sum = resd_compute.sum() / 4/ node

	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ Resd/Sqrt')
	resd_compute_sum += resd_compute.sum() / 4/ node

	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/GEMM')
	resd_compute_sum += resd_compute_sum.sum() / 4 / 2/ node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ Resd/AllReduce')
	resd_comm_sum = resd_comm.sum() / 4 / node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/AllReduce')
	resd_comm_sum += resd_compute.sum() / 4 / 2/ node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/Bcast')
	resd_comm_sum += resd_compute.sum() / 4 / 2/ node

	resd_copy = df[['Times(s)']].where(df['Operations'] == '+ Resd/D2H')
	resd_copy_sum = resd_copy.sum() / 4/ node

	print(node,",ChASE(NCCL),Filter,",filter_compute_sum.values[0],",",filter_comm_sum.values[0],",",filter_copy_sum)
	print(node,",ChASE(NCCL),QR,",qr_compute_sum.values[0],",",qr_comm_sum.values[0],",",qr_copy_sum.values[0])
	print(node,",ChASE(NCCL),RR,",rr_compute_sum.values[0],",",rr_comm_sum.values[0],",",rr_copy_sum.values[0])
	print(node,",ChASE(NCCL),Residual,",resd_compute_sum.values[0],",",resd_comm_sum.values[0],",",resd_copy_sum.values[0])

def No_NCCL_data_retrieve(node, path):
	df = pd.read_csv(path, names=["Operations", "Times(s)"])

	### Filter ###
	filter_compute = df[['Times(s)']].where(df['Operations'] == '+ Filter/GEMM')
	filter_compute_sum = filter_compute.sum()/4 / node

	filter_comm = df[['Times(s)']].where(df['Operations'] == '+ Filter/AllReduce')
	filter_comm_sum = filter_comm.sum()/4/ node

	filter_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/D2H')
	filter_copy_sum = filter_copy.sum()/4/ node

	filter_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/H2D')
	filter_copy_sum += filter_copy.sum()/4/ node

	### QR ###
	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/syherk')
	qr_compute_sum = qr_compute.sum() / 4/ node

	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/Potrf')
	qr_compute_sum += qr_compute.sum() / 4/ node

	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/Trsm')
	qr_compute_sum += qr_compute.sum() / 4/ node

	qr_comm = df[['Times(s)']].where(df['Operations'] == '+ QR/AllReduce')
	qr_comm_sum = qr_comm.sum() / 4/ node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/Memcpy')
	qr_copy_sum = qr_copy.sum() / 4/ node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/H2D')
	qr_copy_sum += qr_copy.sum() / 4/ node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/D2H')
	qr_copy_sum += qr_copy.sum() / 4/ node

	### RR ###
	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ RR/GEMM')
	rr_compute_sum = rr_compute.sum() / 4/ node

	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ RR/HEEVD')
	rr_compute_sum += rr_compute.sum() / 4/ node

	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/GEMM')
	rr_compute_sum += rr_compute.sum() / 4 / 2/ node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ RR/AllReduce')
	rr_comm_sum = rr_comm.sum() / 4/ node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/AllReduce')
	rr_comm_sum += rr_comm.sum() / 4 / 2/ node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/Bcast')
	rr_comm_sum += rr_comm.sum() / 4 / 2/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/D2H')
	rr_copy_sum = rr_copy.sum() / 4/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/H2D')
	rr_copy_sum += rr_copy.sum() / 4/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/Memcpy')
	rr_copy_sum += rr_copy.sum() / 4/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/H2D')
	rr_copy_sum += rr_copy.sum() / 4/ 2/ node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/D2H')
	rr_copy_sum += rr_copy.sum() / 4/ 2/ node

	### Residual ###
	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ Resd/Residual')
	resd_compute_sum = resd_compute.sum() / 4/ node

	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ Resd/Sqrt')
	resd_compute_sum += resd_compute.sum() / 4/ node

	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/GEMM')
	resd_compute_sum += resd_compute_sum.sum() / 4 / 2/ node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ Resd/AllReduce')
	resd_comm_sum = resd_compute.sum() / 4/ node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/AllReduce')
	resd_comm_sum += resd_compute.sum() / 4 / 2/ node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/Bcast')
	resd_comm_sum += resd_compute.sum() / 4 / 2/ node

	resd_copy = df[['Times(s)']].where(df['Operations'] == '+ asynCxHGatherC/D2H')
	resd_copy_sum = resd_copy.sum() / 4/ 2 / node

	print(node,",ChASE(w/o NCCL),Filter,",filter_compute_sum.values[0],",",filter_comm_sum.values[0],",",filter_copy_sum.values[0])
	print(node,",ChASE(w/o NCCL),QR,",qr_compute_sum.values[0],",",qr_comm_sum.values[0],",",qr_copy_sum.values[0])
	print(node,",ChASE(w/o NCCL),RR,",rr_compute_sum.values[0],",",rr_comm_sum.values[0],",",rr_copy_sum.values[0])
	print(node,",ChASE(w/o NCCL),Residual,",resd_compute_sum.values[0],",",resd_comm_sum.values[0],",",resd_copy_sum.values[0])

def OLD_NCCL_data_retrieve(node, path):
	df = pd.read_csv(path, names=["Operations", "Times(s)"])

	### Filter ###
	filter_compute = df[['Times(s)']].where(df['Operations'] == '+ Filter/GEMM')
	filter_compute_sum = filter_compute.sum() / node

	filter_comm = df[['Times(s)']].where(df['Operations'] == '+ Filter/AllReduce')
	filter_comm_sum = filter_comm.sum()/ node

	filter_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/D2H')
	filter_copy_sum = filter_copy.sum()/ node

	filter_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/H2D')
	filter_copy_sum += filter_copy.sum()/ node

	filter_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/Memcpy')
	filter_copy_sum += filter_copy.sum()/ node

	### QR ###
	qr_compute = df[['Times(s)']].where(df['Operations'] == '+ QR/geqrf')
	qr_compute_sum = qr_compute.sum() / node

	qr_comm = df[['Times(s)']].where(df['Operations'] == '+ QR/Bcast')
	qr_comm_sum = qr_comm.sum() / node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/Memcpy')
	qr_copy_sum = qr_copy.sum() / node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/H2D')
	qr_copy_sum += qr_copy.sum() / node

	qr_copy = df[['Times(s)']].where(df['Operations'] == '+ QR/D2H')
	qr_copy_sum += qr_copy.sum() / node

	### RR ###
	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ RR/GEMM')
	rr_compute_sum = rr_compute.sum() / node

	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ Filter/GEMM')
	rr_compute_sum += rr_compute.mean()

	rr_compute = df[['Times(s)']].where(df['Operations'] == '+ RR/HEEVD')
	rr_compute_sum += rr_compute.sum() / node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ RR/Bcast')
	rr_comm_sum = rr_comm.sum() / node

	rr_comm = df[['Times(s)']].where(df['Operations'] == '+ Filter/AllReduce')
	rr_comm_sum += rr_comm.mean()

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/D2H')
	rr_copy_sum = rr_copy.sum() / node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/H2D')
	rr_copy_sum += rr_copy.sum() / node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ RR/Memcpy')
	rr_copy_sum += rr_copy.sum() / node

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/D2H')
	rr_copy_sum += rr_copy.mean()

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/H2D')
	rr_copy_sum += rr_copy.mean()

	rr_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/Memcpy')
	rr_copy_sum += rr_copy.mean()

	### Residual ###
	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ Resd/Residual')
	resd_compute_sum = resd_compute.sum() / node

	resd_compute = df[['Times(s)']].where(df['Operations'] == '+ Filter/GEMM')
	resd_compute_sum += resd_compute.mean()

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ Resd/Bcast')
	resd_comm_sum = resd_comm.sum() / node

	resd_comm = df[['Times(s)']].where(df['Operations'] == '+ Filter/AllReduce')
	resd_comm_sum += resd_comm.mean()

	resd_copy = df[['Times(s)']].where(df['Operations'] == '+ Resd/Memcpy')
	resd_copy_sum = resd_copy.sum() / node

	resd_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/D2H')
	resd_copy_sum += resd_copy.mean()

	resd_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/H2D')
	resd_copy_sum += resd_copy.mean()

	resd_copy = df[['Times(s)']].where(df['Operations'] == '+ Filter/Memcpy')
	resd_copy_sum += resd_copy.mean()

	print(node,",ChASE(v1.2.1),Filter,",filter_compute_sum.values[0],",",filter_comm_sum.values[0],",",filter_copy_sum.values[0])
	print(node,",ChASE(v1.2.1),QR,",qr_compute_sum.values[0],",",qr_comm_sum.values[0],",",qr_copy_sum.values[0])
	print(node,",ChASE(v1.2.1),RR,",rr_compute_sum.values[0],",",rr_comm_sum.values[0],",",rr_copy_sum.values[0])
	print(node,",ChASE(v1.2.1),Residual,",resd_compute_sum.values[0],",",resd_comm_sum.values[0],",",resd_copy_sum.values[0])

if __name__ == "__main__":

	original_stdout = sys.stdout 
	
	with open('../../results/comm_vs_compute_vs_cpy.csv', 'w') as f:
		sys.stdout = f
		print("Nodes,Impls,Kernels,Compt.,Comm.,Copy")
		NCCL_data_retrieve(1, './nccl/1/profil.out')
		NCCL_data_retrieve(4, './nccl/4/profil.out')
		NCCL_data_retrieve(16, './nccl/16/profil.out')
		NCCL_data_retrieve(64, './nccl/64/profil.out')
		No_NCCL_data_retrieve(1, './no-nccl/1/profil.out')
		No_NCCL_data_retrieve(4, './no-nccl/4/profil.out')
		No_NCCL_data_retrieve(16, './no-nccl/16/profil.out')
		No_NCCL_data_retrieve(64, './no-nccl/64/profil.out')
		OLD_NCCL_data_retrieve(1, './v1.2.1/1/profil.out')
		OLD_NCCL_data_retrieve(4, './v1.2.1/4/profil.out')
		OLD_NCCL_data_retrieve(16, './v1.2.1/16/profil.out')
		OLD_NCCL_data_retrieve(64, './v1.2.1/64/profil.out')

		sys.stdout = original_stdout 

	


