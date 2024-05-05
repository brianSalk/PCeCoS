import numpy as np


class Matrix:
    def __init__(self, shape: tuple[int, int], resupply_rate, ):
        self.shape = shape
        self.matrix = self._calculate_matrix()
        self.resupply_rate = resupply_rate

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def _calculate_matrix(self):
        return np.pad(np.ones(self.shape), [(1, 1), (1, 1)], 'constant', constant_values=-1)

    def resupply(self):
        self.matrix[(self.matrix < 1) & (0 <= self.matrix)] += self.resupply_rate
