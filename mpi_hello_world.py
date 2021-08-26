from mpi4py import MPI

comm = MPI.COMM_WORLD
process = comm.Get_rank()

print(f"Hello world from {process = }")
