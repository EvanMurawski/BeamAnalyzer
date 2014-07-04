__author__ = 'Evan Murawski'

from interactions import *

from beam import Beam

from solver import Solver, SolverError

my_beam = Beam(10)

my_beam.add_interaction(Force(0,0,False))

my_beam.add_interaction(Force(0,-3))

my_beam.add_interaction(Force(3,7))

my_beam.add_interaction(Force(7,8))

my_beam.add_interaction(Force(10,0,False))

my_beam.add_interaction(Moment(10,36))

Solver.solve(my_beam.interactions)

for item in my_beam.interactions:
	print(item.location, item.magnitude, item.known)

