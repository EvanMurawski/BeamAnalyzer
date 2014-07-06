__author__ = 'Evan Murawski'

from interactions import *
from tabulate import tabulate

class Beam:

    def __init__(self, length):
        """Create a beam object with specified length, starts with
        no interactions, zero knowns and unknowns"""

        self.length = length
        self.interactions = []

    def add_interaction(self, interaction):
        """Adds a single interaction to the beam. Raises an exception if the interaction's location is past
        the end of the beam. Sorts the list of interactions
        by location, ascending"""

        if interaction.location > self.length:
            raise InteractionLocationError(interaction.location)

        self.interactions.append(interaction)

        self.interactions.sort(key=lambda item: item.location)


    def add_list_interactions(self, list_interactions):
        """Adds a list of interactions to the beam. Raises an exception if the interaction's location is 
        past the end of the beam. Sorts the list of interactions
        by location, ascending."""

        for interaction in list_interactions:
            if interaction.location > self.length:
                raise InteractionLocationError(interaction.location)

        for interaction in list_interactions:
            self.interactions.append(interaction)

        self.interactions.sort(key=lambda item: item.location)

    def __str__(self):

        table = [[item.__class__.__name__,
                 item.location, 
                 item.magnitude if item.known else 'N/A',
                 "Known" if item.known else "Unknown"] 
                 for item in self.interactions]

        return tabulate(table, headers= ["", "Location", "Magnitude", "Known"])


    def count_knowns(self):
        knowns = 0
        for item in self.interactions:
            if item.known:
                knowns += 1

        return knowns

    def count_unknowns(self):
        unknowns = 0
        for item in self.interactions:
            if not item.known:
                unknowns += 1

        return unknowns









