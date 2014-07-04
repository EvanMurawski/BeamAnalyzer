__author__ = 'Evan Murawski'


class InteractionLocationError(Exception):

    def __init__(self, value):
        self.value = value

class Interaction:

    def __init__(self, location, magnitude, known=True):

        if location < 0:
            raise InteractionLocationError(location)

        self.location = location
        self.magnitude = magnitude
        self.known = known


class Force(Interaction):

    def __init__(self, location, magnitude, known=True):
        Interaction.__init__(self, location, magnitude, known)

class Moment(Interaction):

    def __init__(self, location, magnitude, known=True):
        Interaction.__init__(self, location, magnitude, known)