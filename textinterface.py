__author__ = 'Evan Murawski'

from beam import Beam

from interactions import *

import sys

def request_num(prompt, has_limits=False, min=0, max=0, ):

	valid_input = False

	while not valid_input:

		try:
			response = float(input(prompt))
		except ValueError:
			print('Must be a number.')
			continue

		if has_limits:
			if response >=min and response <= max:
				valid_input = True
			else:
				print('Response not in valid range.')
		else:
			valid_input = True

	return response

def request_interaction(beam):
	
	valid_input = False

	while not valid_input:
		resp = input("Enter 'f' to enter a point force or 'm' to enter a point moment: ").lower()

		if resp not in ['f', 'm']:
			print('Invalid response.')
		else:
			valid_input = True


	if resp == 'f':
		location = request_num('Enter the location of the force: ', True, 0, beam.length)
		magnitude = request_num('Enter the magnitude of the force (0 for an unknown force): ')
		
		if magnitude == 0:
			beam.add_interaction(Force(location, magnitude, False))
		else:
			beam.add_interaction(Force(location, magnitude))

print('Welcome to BeamAnalyzer vAlpha\n')

length = request_num('Please enter the length of the beam: ', True, 0, sys.float_info.max)
beam = Beam(length)

print("Beam created.\n\nType 'help' for a list of commands, 'q' to quit.")

quit = False

while not quit:

	request = input('Please enter a command: ').lower()

	if request in ['h', 'he', 'hel', 'help']:
		print('insert help here')

	elif request in ['q', 'qu', 'qui', 'quit']
		quit = True

	elif request in ['a', 'ad', 'add']:
		request_interaction(beam)

	else:
		print('Invalid command.')

