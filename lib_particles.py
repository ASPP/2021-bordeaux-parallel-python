import numpy as np
import time


class Particle:
    def __init__(self, idx, x):
        self.idx = idx
        self.x = x

    def __repr__(self):
        return f"Particle({self.idx}, {np.round(self.x, 3)})"


def propagate_particle(particle):
    time.sleep(0.2)  # imitate expensive computation
    particle.x += np.random.normal(scale=0.02)
    if particle.x < 0:
        particle.x = 0.0
    if particle.x > 1:
        particle.x = 1.0 - 1e-8
    return particle
