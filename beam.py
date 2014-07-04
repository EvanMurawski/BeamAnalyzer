__author__ = 'Evan Murawski'

from interactions import Interaction, InteractionLocationError, Force, Moment

import numpy as np

class SolverError(Exception):
    pass

class Beam:

    def __init__(self, length):
        """Create a beam object with specified length, starts with
        no interactions, zero knowns and unknowns"""

        self.length = length
        self.interactions = []
        self.knowns = 0
        self.unknowns = 0

    def add_interaction(self, interaction):
        """Adds a single interaction to the beam. Raises an exception if the interaction's location is past
        the end of the beam. Increments either knows or unknowns as necessary. Sorts the list of interactions
        by location, ascending"""

        if interaction.location > self.length:
            raise InteractionLocationError(interaction.location)

        self.interactions.append(interaction)

        if interaction.known:
            self.knowns += 1
        else:
            self.unknowns += 1

        self.interactions.sort(key=lambda item: item.location)


    def add_list_interactions(self, list_interactions):
        """Adds a list of interactions to the beam. Raises an exception if the interaction's location is 
        past the end of the beam. Increments the knowns and unknowns as necessary. Sorts the list of interactions
        by location, ascending."""

        for interaction in list_interactions:
            if interaction.location > self.length:
                raise InteractionLocationError(interaction.location)

        for interaction in list_interactions:
            self.interactions.append(interaction)

            if interaction.known:
                self.knowns += 1
            else:
                self.unknowns += 1

        self.interactions.sort(key=lambda item: item.location)

    def solve(self):

        if(self.unknowns != 2):
            raise SolverError('There must be 2 unknowns.')

        unknown_forces = []
        unknown_moments = []

        known_interactions = list(self.interactions)

        for interaction in self.interactions:
            if not interaction.known:
                if isinstance(interaction, Force):
                    unknown_forces.append(interaction)
                if isinstance(interaction, Moment):
                    unknown_moments.append(interaction)

                known_interactions.remove(interaction)

        #Case 1: 2 unknown forces
        if len(unknown_forces) == 2 and len(unknown_moments) == 0:

            #define elements of matrices
            a_1_1 = 1
            a_1_2 = 1

            a_2_1 = unknown_forces[0].location
            a_2_2 = unknown_forces[1].location

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

            a = np.array([[a_1_1, a_1_2], [a_2_1, a_2_2]])
            b = np.array([b_1, b_2])

            try:
                x = np.linalg.solve(a, b)
            except LinAlgError:
                raise SolverError('Something went wrong with the linear algebra.')

            unknown_forces[0].magnitude = x[0]
            unknown_forces[0].known = True
            unknown_forces[1].magnitude = x[1]
            unknown_forces[1].known = True

            return self.interactions








