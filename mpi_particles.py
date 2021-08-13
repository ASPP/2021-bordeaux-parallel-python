from mpi4py import MPI
import numpy as np
import time

from lib_particles import Particle, propagate_particle


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_ranks = comm.Get_size()

np.random.seed(1235 + rank)

n_particles = 12
n_steps = 5

# determine work distribution between ranks
n_particles_per_process = int(np.ceil(n_particles / n_ranks))
x_min = rank / n_ranks
x_max = x_min + 1 / n_ranks

# initialize local particles assuming homogeneity
local_particles = [
    Particle(n_particles_per_process * rank + idx, np.random.uniform(x_min, x_max))
    for idx in range(n_particles_per_process)
]
print(f"initial configuration ({rank=}):",
      list(sorted(local_particles, key=lambda p: p.idx)))

# simulate for a couple of time steps
for step in range(n_steps):

    # propagate particle positions
    for particle in local_particles:
        particle = propagate_particle(particle)

    # communicate particle positions
    local_particles_new = []
    for root in range(n_ranks):
        recv_buffer = comm.bcast(local_particles, root=root)
        for particle_new in recv_buffer:
            if x_min <= particle_new.x < x_max:
                local_particles_new.append(particle_new)
    local_particles = local_particles_new

    print()
    print(f"{step=} ({rank=}):",
          list(sorted(local_particles, key=lambda p: p.idx)))
