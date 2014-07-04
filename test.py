__author__ = 'Evan Murawski'

from interactions import *

from beam import Beam

from solver import Solver, SolverError

my_beam = Beam(30)

my_beam.add_interaction(Force(0,0,False))
my_beam.add_interaction(Force(10,-100))
my_beam.add_interaction(Force(20,200))
my_beam.add_interaction(Force(30, -300))
my_beam.add_interaction(Moment(0,0,False))

Solver.solve(my_beam.interactions)

for item in my_beam.interactions:
	print(item.__class__.__name__, item.location, item.magnitude, item.known)
