"""A text based UI, implemented with cmd2: https://bitbucket.org/catherinedevlin/cmd2

BeamAnalyzer v0.1.0
Copyright 2014 Evan Murawski
License: MIT
"""
__author__ = 'Evan Murawski'

from beam import Beam
from interactions import InteractionLocationError, Interaction, Force, Moment, Dist_Force
import cmd2 as cmd
from cmd2 import options, make_option
import solver
from solver import SolverError
import shearmomentgenerator
from shearmomentgenerator import Shear_Moment_Error
import matplotlib.pyplot as plt
import numpy as np

class Text_Interface(cmd.Cmd):
    """Defines the text UI, using cmd2"""

    #Contains the active beam
    beam = None

    PLOT_MARGIN = 0.15

    def preloop(self):
        """Before the loop starts: Request the beam length from the 
        user and create a new beam.
        """

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
        """Add a force. Usage: 
        Add a known force: addf location magnitude
        Add an unknown force: addf location
        """

        list_args = str.split(arguments)
        float_args = []

        #Attempt to convert arguments to floating point numbers.
        try:
            for item in list_args:
                float_args.append(float(item))
        except ValueError:
            print("Arguments must be numers.")
            return

        #Determine if this will be a known or unknown force.
        if len(list_args) == 1:
            known = False
            float_args.append(float(0))
        elif len(list_args) == 2:
            known = True
        else:
            print("Arguments must be 1 or 2 numbers.")
            return

        #Add the force.
        try:
            self.beam.add_interaction(Force(float_args[0], float_args[1], known))
        except InteractionLocationError:
            print("Invalid location for force.")
            return

        print("Added.") 

    def do_addm(self, arguments):
        """Add a moment. Usage: 
        Add a known moment: addm location magnitude
        Add an unknown moment: addm location
        """

        list_args = str.split(arguments)
        float_args = []

        #Attempt to convert the args to floating point numbers.
        try:
            for item in list_args:
                float_args.append(float(item))
        except ValueError:
            print("Arguments must be numers.")
            return

        #Determine if this is a known or unknown moment.
        if len(list_args) == 1:
            known = False
            float_args.append(float(0))
        elif len(list_args) == 2:
            known = True
        else:
            print("Arguments must be 1 or 2 numbers.")
            return

        #Add the moment.
        try:
            self.beam.add_interaction(Moment(float_args[0], float_args[1], known))
        except InteractionLocationError:
            print("Invalid location for moment.")
            return

        print("Added.") 

    def do_adddf(self, arguments):
        """Add a distributed force. Usage: 
        Add a distributed force: addf start magnitude end
        """

        list_args = str.split(arguments)
        float_args = []

        #Attempt to convert arguments to floating point numbers.
        try:
            for item in list_args:
                float_args.append(float(item))
        except ValueError:
            print("Arguments must be numers.")
            return

        #Determine if this will be a known or unknown force.
        if len(list_args) != 3:
            print("Arguments must be 3 numbers.")
            return

        #Add the force.
        try:
            self.beam.add_interaction(Dist_Force(float_args[0], float_args[1], float_args[2]))
        except InteractionLocationError:
            print("Invalid location for distributed force.")
            return

        print("Added.")


    def do_view(self, arguments):
        """View the current status of the beam."""

        print("\n", self.beam, "\n")    
        print("Unknowns: ",self.beam.count_unknowns(), "\n")   

    def do_solve(self, arguments):
        """Solve the current beam."""

        solver.solve(self.beam)
        self.do_view(None)

    def do_reset(self, arguments):
        """Reset the beam - lets you create a new beam."""

        self.preloop()
        print('Beam reset.')

    @options([make_option('-s', '--step', type="float", help="Specify the step size."),
            make_option('-a', '--annotate', action="store_true", help="Annotate key points on the graph.")])
    def do_plot(self, arguments, opts=None):
        """Plot the shear / moment diagram. Usage:
        plot [-s stepsize] (default step size 0.01)
        """

        step_size = 0.01

        annotate = False

        if opts.step != None:
            step_size = opts.step

        if opts.annotate != None:
            annotate = True

        #Generate the shear and moment points, using generate_numerical
        shear_moment = shearmomentgenerator.generate_numerical(self.beam, step_size)

        #Plot the points
        x = np.arange(0, self.beam.length, step_size)

        shear = [y[0] for y in shear_moment]
        moment = [y[1] for y in shear_moment]

        fig = plt.figure()

        shear_plot = fig.add_subplot(211)
        shear_plot.plot(x, shear)
        plt.title('Shear')

        moment_plot = fig.add_subplot(212)
        moment_plot.plot(x, moment)
        plt.title('Moment')

        if annotate:
            for interaction in self.beam.interactions:
                point_one = int(interaction.location / step_size) - 1
                point_two = int(interaction.location / step_size)
    
                
                shear_plot.annotate('(' + str(interaction.location) + 
                    ', ' + str(shear[point_one]) + ')', xy=(interaction.location, shear[point_one]), textcoords='offset points')
    
                if isinstance(interaction, Moment):
                    moment_plot.annotate('(' + str(interaction.location) + 
                        ', ' + str(moment[point_one]) + ')', xy=(interaction.location, moment[point_one]), textcoords='offset points')
    
                if interaction.location != self.beam.length:
                    shear_plot.annotate('(' + str(interaction.location) + 
                        ', ' + str(shear[point_two]) + ')', xy=(interaction.location, shear[point_two]), textcoords='offset points')
    
                    moment_plot.annotate('(' + str(interaction.location) + 
                        ', ' + str(moment[point_two]) + ')', xy=(interaction.location, moment[point_two]), textcoords='offset points')


        shear_plot.axis([min(x), max(x), min(shear) - self.PLOT_MARGIN * (max(shear)-min(shear)), max(shear) + self.PLOT_MARGIN * (max(shear)-min(shear))])
        moment_plot.axis([min(x), max(x), min(moment) - self.PLOT_MARGIN * (max(moment)-min(moment)), max(moment) + self.PLOT_MARGIN * (max(moment)-min(moment))])

        plt.show()

if __name__ == '__main__':
    """The main method."""

    interface = Text_Interface()
    interface.cmdloop()



