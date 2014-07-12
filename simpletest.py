__author__ = 'Evan Murawski'

import unittest

from interactions import *

from beam import Beam
import solver
from solver import SolverError

import shearmomentgenerator
from shearmomentgenerator import Shear_Moment_Error
import matplotlib.pyplot as plt
import numpy as np

step_size = 0.001

beam = Beam(30)

beam.add_interaction(Force(0, 0, False))
beam.add_interaction(Force(20, 0, False))
beam.add_interaction(Dist_Force(0, -1, 10))
beam.add_interaction(Force(15, -20))
beam.add_interaction(Force(30, -10))

solver.solve(beam)

print(beam)

shear_moment = shearmomentgenerator.generate_numerical(beam, step_size)

#Plot the points
x = np.arange(0, beam.length, step_size)

shear = [y[0] for y in shear_moment]
moment = [y[1] for y in shear_moment]

plt.subplot(2,1,1)
plt.plot(x, shear)
plt.title('Shear')

plt.subplot(2, 1, 2)
plt.plot(x, moment)
plt.title('Moment')

plt.show()