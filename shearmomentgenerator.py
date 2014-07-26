"""Contains the classes and functions for generating shear and moment diagrams. Currently only supports 
point forces and moments.
"""
__author__ = 'Evan Murawski'

from beam import Beam
from interactions import Interaction, InteractionLocationError, Force, Moment, Dist_Force
import solver
from solver import SolverError
import numpy as np

class Shear_Moment_Error(Exception):
    """Errors for the shear / moment generator"""
    pass


#clever method - not currently available from UI. May get more difficult to use
#after I add distributed forces. Also somewhat pointless, since moments almost
#have to be done numerically. 
def generate_shear(beam):
    """Cleverly generates shear points for the given beam, returned as a list of 2-tuples in
    the format (location, magnitude)
    """

    for interaction in beam.interactions:
        if not interaction.known:
            raise Shear_Moment_Error('Cannot generate shear diagram for an unsolved beam.')

    shear_points = []

    shear_points.append((0,0))
    curr_shear = 0

    for item in beam.interactions:
        if(isinstance(item, Force)):
            if item.location != 0:
                shear_points.append((item.location, curr_shear))
            curr_shear += item.magnitude
            shear_points.append((item.location, curr_shear))

    shear_points.append((beam.length, 0))

    return shear_points


#Only works for point forces
def gen_sub_beam(beam, sub_length):
    """Generates a subbeam of the given length for purposes
    of generating internal shear and moment points. Currently 
    only supports point loads. Distrubuted loads will make 
    this method a lot more complicated.
    """
    sub_beam = Beam(sub_length)

    for item in beam.interactions:
        if not isinstance(item, Dist_Force):
            if item.location <= sub_length:
                sub_beam.add_interaction(item)

        elif item.location <= sub_length:
            if item.end <= sub_length:
                sub_beam.add_interaction(item)
            else:
                sub_beam.add_interaction(Dist_Force(item.location, item.magnitude, sub_length))

    return sub_beam

#Numerical method
def generate_numerical(beam, step_size):
    """Numerically generates shear and moment points along the length
    of the beam by solving subbeams of increasing length. Step size must
    be specified. step sizes of 0.01 - 0.0001 for a l=10 beam yield reasonable
    solve times on modern CPUs. Returns the result as a list of 2-tuples in the
    format (shear, moment).
    """

    #Verify that the beam is solved.
    for interaction in beam.interactions:
        if not interaction.known:
            raise Shear_Moment_Error('Cannot generate shear diagram for an unsolved beam.')
    
    shear_moment = []

    for curr_size in np.arange(0, beam.length, step_size):
        sub_beam = gen_sub_beam(beam, curr_size)

        #The unknown shear and moment at the end of the cut subbeam.
        internal_shear = Force(curr_size, 0, False)
        internal_moment = Moment(curr_size, 0, False)

        sub_beam.add_interaction(internal_shear)
        sub_beam.add_interaction(internal_moment)

        solver.solve(sub_beam)

        shear_moment.append((-internal_shear.magnitude, internal_moment.magnitude))

    return shear_moment

