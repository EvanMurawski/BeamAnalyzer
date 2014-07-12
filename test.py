__author__ = 'Evan Murawski'

import unittest

from interactions import *

from beam import Beam
import solver
from solver import SolverError

import shearmomentgenerator
from shearmomentgenerator import Shear_Moment_Error


class TestBeamAnalyzer(unittest.TestCase):

	beams = []
	ALMOST = 0.001

	def setUp(self):
		self.beams.append(Beam(10))

		self.beams[0].add_interaction(Force(5, -10))
		self.beams[0].add_interaction(Force(0, 0, False))
		self.beams[0].add_interaction(Force(10, 0, False))

	#A very simple beam with one known force and two unknown forces
	def test_beam0(self):
		solver.solve(self.beams[0])

		#Test solution
		self.assertEqual(5, self.beams[0].interactions[0].magnitude)
		self.assertEqual(5, self.beams[0].interactions[2].magnitude)
		
		shear_moment = shearmomentgenerator.generate_numerical(self.beams[0], 0.01)

		#Test moment
		assert abs(shear_moment[0][1] - 0 ) < self.ALMOST
		assert abs(shear_moment[int(10/0.01/2)][1] - 25) < self.ALMOST
		assert abs(shear_moment[int(10/0.01/4)][1] - 25/2) < self.ALMOST

		#Test shear
		assert abs(shear_moment[1][0] - 5) < self.ALMOST
		assert abs(shear_moment[int(10/0.01/2) -1][0] - 5 ) < self.ALMOST
		assert abs(shear_moment[int(10/0.01/2) +2][0] - (-5)) < self.ALMOST
		assert abs(shear_moment[int(10/0.01) -1][0] - (-5)) < self.ALMOST

	def test_interaction_location_error(self):

		with self.assertRaises(InteractionLocationError):
			Force(-1, 3)

		with self.assertRaises(InteractionLocationError):
			self.beams[0].add_interaction(Force(13, 3))

	def test_solver_error(self):

		self.beams[0].add_interaction(Force(3, 0, False))

		with self.assertRaises(SolverError):
			solver.solve(self.beams[0])

	def test_shear_moment_error(self):

		with self.assertRaises(Shear_Moment_Error):
			shearmomentgenerator.generate_numerical(self.beams[0], 0.01)


if __name__ == '__main__':
	unittest.main()