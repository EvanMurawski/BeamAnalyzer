__author__ = 'Evan Murawski'

from interactions import InteractionLocationError, \
    Interaction, Force, Moment

from beam import Beam, SolverError

my_beam = Beam(10)

my_beam.add_interaction(Force(0,0,False))

my_beam.add_interaction(Force(0,-3))

my_beam.add_interaction(Force(3,7))

my_beam.add_interaction(Force(7,8))

my_beam.add_interaction(Force(10,0,False))

my_beam.add_interaction(Moment(10,36))

my_beam.solve()

for item in my_beam.interactions:
	print(item.location, item.magnitude, item.known)

