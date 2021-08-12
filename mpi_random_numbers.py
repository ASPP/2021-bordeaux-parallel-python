from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

x = np.random.normal(loc=rank, size=10_000)

print(f"Hello world from rank {rank}. My mean is {np.mean(x)}.")
