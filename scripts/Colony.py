import numpy as np
import random


class Colony:
    def __init__(self, initial_coordinates: tuple, color: str, consumption_speed, resource_to_divide):
        self.color = color
        self.cells_number = 1
        self.list_of_cells_coordinates = [initial_coordinates]
        self.feed_list = [0.5]
        self.feed_rate = consumption_speed
        self.resource_to_divide = resource_to_divide

    def divide(self, cell_coords, n_cell, resource_matrix):

        surroundings = resource_matrix[(cell_coords[0] - 1):(cell_coords[0] + 2),
                       (cell_coords[1] - 1):(cell_coords[1] + 2)]
        max_surround = surroundings.max()

        coords_to_divide = random.choice(
            np.argwhere(surroundings == max_surround) - 1)

        self.feed_list.append(self.feed_list[n_cell] / 2)
        self.list_of_cells_coordinates.append(cell_coords + coords_to_divide)
        self.feed_list[n_cell] /= 2
        self.cells_number += 1

    def move(self, coords):
        ...

    def eat(self, resource_matrix):

        if self.cells_number == 0:
            return

        to_delete_list = []

        for n_cell, cell_coords in enumerate(self.list_of_cells_coordinates):
            surroundings = resource_matrix[(cell_coords[0] - 1):(cell_coords[0] + 2),
                           (cell_coords[1] - 1):(cell_coords[1] + 2)]

            coords_w_food = np.argwhere(surroundings > self.feed_rate)

            if coords_w_food.size == 0:
                to_delete_list.append(n_cell)
                self.cells_number -= 1
                continue

            max_surround = surroundings[coords_w_food].max()

            idxs_to_eat = random.choice(
                np.argwhere(surroundings == max_surround) - 1)

            resource_matrix[(cell_coords + idxs_to_eat)] -= self.feed_rate

            self.feed_list[n_cell] += self.feed_rate

            if self.feed_list[n_cell] >= self.resource_to_divide:
                self.divide(cell_coords, n_cell, resource_matrix)

        for index in sorted(to_delete_list, reverse=True):
            del self.list_of_cells_coordinates[index]
            del self.feed_list[index]
