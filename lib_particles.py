import numpy as np
import time


class Particle:
    def __init__(self, idx, x):
        self.idx = idx
        self.x = x

    def __repr__(self):
        return f"Particle({self.idx}, {np.round(self.x, 3)})"


def compute_new_particle_position(x):
    time.sleep(0.2)  # imitate expensive computation
    x += np.random.normal(scale=0.02)
    # x += 0.1 + np.random.normal(scale=0.02)
    if x < 0:
        x = 0.0
    if x >= 1:
        x = 1.0 - 1e-8
    return x
