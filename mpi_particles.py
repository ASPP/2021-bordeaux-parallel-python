from mpi4py import MPI
import numpy as np
import time

from lib_particles import Particle, compute_new_particle_position


comm = MPI.COMM_WORLD
process = comm.Get_rank()
n_processes = comm.Get_size()

# initialize a random number generator for each process
rng = np.random.RandomState(1235 + process)

# define the number of particles per processes and time steps to simulate
n_particles_per_process = 3
n_particles = n_particles_per_process * n_processes
n_time_steps = 5

# determine work distribution between ranks
x_min = process / n_processes
x_max = (process + 1) / n_processes

# initialize local particles assuming homogeneity
local_particles = [
    Particle(n_particles_per_process * process + idx, rng.uniform(x_min, x_max))
    for idx in range(n_particles_per_process)
]
print(
    f"initial configuration ({process=}):",
    list(sorted(local_particles, key=lambda p: p.idx)),
)
# exit()

# simulate dynamics for a couple of time steps
for time_step in range(n_time_steps):

    # propagate particle positions
    for particle in local_particles:
        particle.x = compute_new_particle_position(particle.x)

    # communicate particle positions
    received_particles = []
    for source_process in range(n_processes):
        # we communicate the list `local_particles` from rank `root` to all
        # other ranks; all ranks receive the same list from rank `root`, which
        # is stored in `recv_buffer`; communication is *blocking*, i.e., all
        # ranks wait here until the have received the data
        received_particles += comm.bcast(local_particles, root=source_process)

    assert len(received_particles) == n_particles

    # after the communication is done, we figure out which particles this
    # rank now needs to keep track off
    local_particles = []
    for particle_new in received_particles:
        if x_min <= particle_new.x < x_max:
            local_particles.append(particle_new)

    print()
    print(
        f"{time_step=} ({process=}):",
        list(sorted(local_particles, key=lambda p: p.idx)),
    )
