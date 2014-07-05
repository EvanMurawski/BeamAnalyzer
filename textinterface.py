__author__ = 'Evan Murawski'

from beam import Beam

from interactions import *

import sys

import cmd2 as cmd

from cmd2 import options, make_option

from solver import *

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

    @options([make_option('-f', '--force', action="store_true", help="Add a force."),
              make_option('-m', '--moment', action="store_true", help="Add a moment.")
             ])
    def do_add(self, arguments, opts=None):

        list_args = str.split(arguments)

        float_args = []

        try:
            for item in list_args:
                float_args.append(float(item))

        except ValueError:
            print("Arguments must be numers.")
            return

        if opts == None:
            print("Select either force or moment.")
            return

        if opts.force and opts.moment:
            print("Select either force or moment.")
            return

        if len(list_args) == 1:
            known = False
            float_args.append(float(0))
        elif len(list_args) == 2:
            known = True
        else:
            print("Arguments must be 1 or 2 numbers.")
        

        if opts.force:
            try:
                self.beam.add_interaction(Force(float_args[0], float_args[1], known))
            except InteractionLocationError:
                print("Invalid location for force.")
                return

        elif opts.moment:
            try:
                self.beam.add_interaction(Moment(float_args[0], float_args[1], known))
            except InteractionLocationError:
                print("Invalid location for moment.")
                return    

    #Improve this later: create to string method in beam class.
    def do_view(self, arguments):
        print('Beam Length: ', self.beam.length, '\n\n')

        print('Unknowns: ' + str(self.beam.unknowns)  + '\n\n')

        for item in self.beam.interactions:
            print(item.__class__.__name__, ' , Location: ' + str(item.location), ' , Magnitude: ' + str(item.magnitude) if item.known else '', 'Known: ', item.known)       

    def do_solve(self, arguments):

        Solver.solve(self.beam.interactions)
        self.do_view(None)

if __name__ == '__main__':

    interface = Text_Interface()
    interface.cmdloop()



