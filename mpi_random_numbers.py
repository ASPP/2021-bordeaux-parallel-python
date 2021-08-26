from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD  # get MPI communicator
process = comm.Get_rank()  # get process index
n_processes = comm.Get_size()  # get total number of processes

# initialize a random number generator for each process
rng = np.random.RandomState(1235 + process)

# define the number of particles per processes and time steps to simulate
n_particles_per_process = 3
n_particles = n_particles_per_process * n_processes
n_time_steps = 5

# determine work distribution between ranks
x_min = process / n_processes
x_max = (process + 1) / n_processes

# generate initial positions
x = np.random.uniform(x_min, x_max, size=n_particles_per_process)

print(f"{process=}: particle positions {x}")
