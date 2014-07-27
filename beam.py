"""Contains the Beam class which defines a Beam object"""
__author__ = 'Evan Murawski'

from interactions import InteractionLocationError, Interaction, Force, Moment, Dist_Force
from tabulate import tabulate

class Beam:
    """Defines a beam object which contains a length and a 
    list of interaction objects.
    """

    def __init__(self, length):
        """Create a beam object with specified length, starts with
        no interactions
        """
        self.length = length
        self.interactions = []

    def add_interaction(self, interaction):
        """Adds a single interaction to the beam. Raises an exception if the interaction's location is past
        the end of the beam. Sorts the list of interactions
        by location, ascending"""

        if interaction.location > self.length:
            raise InteractionLocationError(interaction.location)

        if isinstance(interaction, Dist_Force):
            if interaction.end > self.length:
                raise InteractionLocationError(interaction.end)

        self.interactions.append(interaction)

        self.interactions.sort(key=lambda item: item.location)


    def add_list_interactions(self, list_interactions):
        """Adds a list of interactions to the beam. Raises an exception if the interaction's location is 
        past the end of the beam. Sorts the list of interactions
        by location, ascending."""

        for interaction in list_interactions:
            if interaction.location > self.length:
                raise InteractionLocationError(interaction.location)

            if isinstance(interaction, Dist_Force):
                if interaction.end > self.length:
                    raise InteractionLocationError(interaction.end)

        for interaction in list_interactions:
            self.interactions.append(interaction)

        self.interactions.sort(key=lambda item: item.location)

    def __str__(self):
        """A string representation of the beam, using tabulate."""

        table = [item.to_list() for item in self.interactions]

        return tabulate(table, headers= ["", "Location", "Magnitude", "Known"])


    def count_knowns(self):
        """returns the number of known interactions in the beam."""

        knowns = 0
        for item in self.interactions:
            if item.known:
                knowns += 1

        return knowns

    def count_unknowns(self):
        """Returns the number of unknown interactions in the beam."""

        unknowns = 0
        for item in self.interactions:
            if not item.known:
                unknowns += 1

        return unknowns