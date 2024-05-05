#!/usr/bin/env python3

import argparse
import random
import numpy as np
from scripts.Colony import Colony
from scripts.vizualisation import vizualisation
from scripts.Matrix import Matrix

parser = argparse.ArgumentParser(description='Primitive Cell Colony Simulator',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-c', '--colony-number', default=2, help='Number of colonies', type=int, nargs='?')
parser.add_argument('-m', '--matrix-shape', default=(30, 30), help='Matrix shape', type=int, nargs=2)
parser.add_argument('-f', '--frames', default=30, help='Number of rounds (frames)', type=int, nargs='?')
parser.add_argument('-r', '--resupply-rate', default=0.05, help='Resupply rate of resource', type=float, nargs='?')
parser.add_argument('-d', '--division-level', default=1, help='Division resource level', type=float, nargs='?')
parser.add_argument('--output', default='animation.gif', help='Output filename', type=str, nargs='?')

args = parser.parse_args()

COLONIES_NUMBER = args.colony_number
MATRIX_SHAPE = args.matrix_shape
ROUNDS_NUMBER = args.frames
RESUPPLY_RATE = args.resupply_rate
DIVISION_RESOURCE_LEVEL = args.division_level

colony_colors = ['red', 'green', 'blue',
                 'orange', 'violet', 'yellow']

resource_matrix = Matrix(MATRIX_SHAPE, RESUPPLY_RATE)

colonies_idxs = np.random.randint(1, resource_matrix.shape, (COLONIES_NUMBER, 2))

list_of_colonies = []

for i, initial_coords in enumerate(colonies_idxs):
    consumption_speed = random.uniform(0.1, 0.3)

    list_of_colonies.append(Colony(initial_coords,
                                   colony_colors[i],
                                   consumption_speed,
                                   DIVISION_RESOURCE_LEVEL))

    print(colony_colors[i], consumption_speed)

vizualisation(list_of_colonies, resource_matrix, ROUNDS_NUMBER, file_name=args.output)
