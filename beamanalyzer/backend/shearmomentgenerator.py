"""Contains the classes and functions for generating shear and moment diagrams. Currently only supports 
point forces and moments.
"""

__author__ = 'Evan Murawski'

try:
    from beamanalyzer.backend.beam import Beam
    from beamanalyzer.backend.interactions import Interaction, InteractionLocationError, Force, Moment, Dist_Force
    import beamanalyzer.backend.solver as solver
    from beamanalyzer.backend.solver import SolverError
except ImportError:
    from backend.beam import Beam
    from backend.interactions import Interaction, InteractionLocationError, Force, Moment, Dist_Force
    import backend.solver as solver
    from backend.solver import SolverError

import numpy as np


class Shear_Moment_Error(Exception):
    """Errors for the shear / moment generator"""
    pass


#Only works for point forces
def gen_sub_beam(beam, sub_length):
    """Generates a subbeam of the given length for purposes
    of generating internal shear and moment points.
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
    format (shear, moment). One point for each step, from 0 to beam.length.
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