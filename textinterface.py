__author__ = 'Evan Murawski'

from beam import Beam

from interactions import *

import sys

import cmd2 as cmd

from cmd2 import options, make_option

from solver import *

from shearmomentgenerator import Shear_Moment_Generator

import matplotlib.pyplot as plt

class Text_Interface(cmd.Cmd):

    beam = None

    def preloop(self):
        valid = False

        while not valid:
            try: 
                length = float(input('Enter the length of the beam: '))
            except ValueError:
                print('Length must be a positive number.')
                continue

            if length > 0:
                self.beam = Beam(length)
                valid = True
            else:
                print('Length must be a positive number.')

    def do_addf(self, arguments):
        """Add a force."""

        list_args = str.split(arguments)

        float_args = []

        try:
            for item in list_args:
                float_args.append(float(item))

        except ValueError:
            print("Arguments must be numers.")
            return


        if len(list_args) == 1:
            known = False
            float_args.append(float(0))
        elif len(list_args) == 2:
            known = True
        else:
            print("Arguments must be 1 or 2 numbers.")
            return

        try:
            self.beam.add_interaction(Force(float_args[0], float_args[1], known))
        except InteractionLocationError:
            print("Invalid location for force.")
            return

        print("Added.") 

    def do_addm(self, arguments):
        """Add a moment."""

        list_args = str.split(arguments)

        float_args = []

        try:
            for item in list_args:
                float_args.append(float(item))

        except ValueError:
            print("Arguments must be numers.")
            return


        if len(list_args) == 1:
            known = False
            float_args.append(float(0))
        elif len(list_args) == 2:
            known = True
        else:
            print("Arguments must be 1 or 2 numbers.")
            return

        try:
            self.beam.add_interaction(Moment(float_args[0], float_args[1], known))
        except InteractionLocationError:
            print("Invalid location for moment.")
            return

        print("Added.") 


    def do_view(self, arguments):
        """View the current status of the beam."""

        print("\n", self.beam, "\n")    
        print("Unknowns: ",self.beam.count_unknowns(), "\n")   

    def do_solve(self, arguments):
        """Solve the current beam."""

        Solver.solve(self.beam.interactions)
        self.do_view(None)

    def do_reset(self, arguments):
        """Reset the beam."""

        self.preloop()
        print('Beam reset.')

    def do_shearplot(self, arguments):
        """Generate shear plot"""

        shear_points = Shear_Moment_Generator.generate_shear(self.beam)
        print(shear_points)

        x,y = zip(*shear_points)
        plt.plot(x,y)
        plt.show()

if __name__ == '__main__':

    interface = Text_Interface()
    interface.cmdloop()



