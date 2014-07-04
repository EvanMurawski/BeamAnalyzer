__author__ = 'Evan Murawski'

from interactions import *

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











