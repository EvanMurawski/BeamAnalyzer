"""Contains the classes and functions used to solve a Fbeam with two unknown interactions. 
Currently supports 2 unknown forces or 1 unknown moment and 1 unknown force. There
is currently no support for distributed forces.
"""
__author__ = 'Evan Murawski'

import numpy as np
from backend.interactions import InteractionLocationError, Interaction, Force, Moment, Dist_Force
from backend.beam import Beam

class SolverError(Exception):
    """Solver Errors"""
    pass


def sum_knowns(known_interactions):
    """Individually sums the magnitudes of the known forces and known moments it is passed. 
    returns these as a numpy array object in format ([-sum_known forces, -sum_known_moments])
    """

    sum_known_forces = 0
    sum_known_moments = 0

    for item in known_interactions:
        if isinstance(item, Force):
            sum_known_forces += item.magnitude
            sum_known_moments += item.magnitude * item.location
        if isinstance(item, Moment):
            sum_known_moments += item.magnitude

    b_1 = -sum_known_forces
    b_2 = -sum_known_moments
    
    return np.array([b_1, b_2])


def pointify_interactions(original_interactions):
    """Returns a list of interactions, with all distributed forces changed to point forces
    at their average action point. Does not modify the beam."""

    pointified_interactions = []

    for interaction in original_interactions:
        if not isinstance(interaction, Dist_Force):
            pointified_interactions.append(interaction)
        else:
            pointified_magnitude = interaction.magnitude * (interaction.end - interaction.location)
            pointified_location = (interaction.end + interaction.location)/2
            pointified_interactions.append(Force(pointified_location, pointified_magnitude))

    return pointified_interactions


def solve(beam):
    """Solves a list of interactions with 2 unknowns. Modifies the list
    it is passed to contain the solved quantities, with known = True. Returns 
    the modified list. Also modifies the beam."""

    list_interactions = pointify_interactions(beam.interactions)

    unknown_forces = []
    unknown_moments = []

    known_interactions = list(list_interactions)

    for interaction in list_interactions:
        if not interaction.known:
            if isinstance(interaction, Force):
                unknown_forces.append(interaction)
            if isinstance(interaction, Moment):
                unknown_moments.append(interaction)

            known_interactions.remove(interaction)

    if (len(unknown_forces) + len(unknown_moments) != 2):
        raise SolverError('There must be 2 unknowns.')

    #Case 1: 2 unknown forces
    if len(unknown_forces) == 2 and len(unknown_moments) == 0:

        #define elements of matrices
        a_1_1 = 1
        a_1_2 = 1

        a_2_1 = unknown_forces[0].location
        a_2_2 = unknown_forces[1].location

        a = np.array([[a_1_1, a_1_2], [a_2_1, a_2_2]])
        b = sum_knowns(known_interactions)

        try:
            x = np.linalg.solve(a, b)
        except LinAlgError:
            raise SolverError('Something went wrong with the linear algebra.')

        unknown_forces[0].magnitude = x[0]
        unknown_forces[0].known = True
        unknown_forces[1].magnitude = x[1]
        unknown_forces[1].known = True

        return list_interactions

    #Case 2: 1 unknown force and 1 unknown moment
    elif len(unknown_forces) == 1 and len(unknown_moments) == 1:

        #Define elements of matricies
        a_1_1 = 0
        a_1_2 = 1
        a_2_1 = 1
        a_2_2 = unknown_forces[0].location

        b = sum_knowns(known_interactions)
        a = np.array([[a_1_1, a_1_2], [a_2_1, a_2_2]])

        try:
            x = np.linalg.solve(a, b)
        except LinAlgError:
            raise SolverError('Something went wrong with the linear algebra.')

        unknown_moments[0].magnitude = x[0]
        unknown_moments[0].known = True
        unknown_forces[0].magnitude = x[1]
        unknown_forces[0].known = True

        return list_interactions

    #Unsupported case
    else:
        raise SolverError('Unsupported case: only 1F,1M and 2F supported.')