"""Defines the types of interactions a beam can have. Currently supports 
only point forces and moments.
"""
__author__ = 'Evan Murawski'


class InteractionLocationError(Exception):
    """Error for invalid interaction locations. Contains the invalid
    location as 'value'
    """

    def __init__(self, value):
        self.value = value

class Interaction:
    """A general interaction object. All specific interactions
    are subclasses of Interaction.
    """

    def __init__(self, location, magnitude, known=True):
        """Create a general interaction object. Location must 
        be >= 0
        """

        if location < 0:
            raise InteractionLocationError(location)

        self.location = location
        self.magnitude = magnitude
        self.known = known


class Force(Interaction):
    """A point force. Subclass of Interaction"""

    def __init__(self, location, magnitude, known=True):
        Interaction.__init__(self, location, magnitude, known)

class Moment(Interaction):
    """A point moment. Subclass of Interaction"""

    def __init__(self, location, magnitude, known=True):
        Interaction.__init__(self, location, magnitude, known)


class Dist_Force(Interaction):
    """A distributed force. Subclass of Interaction. Must be known."""

    def __init__(self, location, magnitude, end):

        if(end < location):
            raise InteractionLocationError(end)

        Interaction.__init__(self, location, magnitude, True)
        self.end = end