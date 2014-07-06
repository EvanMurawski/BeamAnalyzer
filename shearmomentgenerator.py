__author__ = 'Evan Murawski'

from beam import Beam
from interactions import *

class ShearMomentError(Exception):
    pass

class Shear_Moment_Generator:

    @staticmethod
    def generate_shear(beam):

        for interaction in beam.interactions:
            if not interaction.known:
                raise ShearMomentError('Cannot generate shear diagram for an unsolved beam.')

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