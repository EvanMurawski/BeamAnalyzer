__author__ = 'Evan Murawski'

import numpy as np

from interactions import *

class SolverError(Exception):
    pass

class Solver:

    @staticmethod
    def sum_knowns(known_interactions):

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



    @staticmethod
    def solve(list_interactions):
        """Solves a list of interactions with 2 unknowns. Modifies the list
        it is passed to contain the solved quantities, with known = True. Returns 
        the modified list."""


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
            b = Solver.sum_knowns(known_interactions)

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

            a_1_1 = 0
            a_1_2 = 1
            a_2_1 = 1
            a_2_2 = unknown_forces[0].location

            b = Solver.sum_knowns(known_interactions)
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

        else:
            raise SolverError('Unsupported case: only 1F,1M and 2F supported.')