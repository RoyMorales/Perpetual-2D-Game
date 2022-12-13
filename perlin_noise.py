# Perlin Noise Generator

import random


class PerlinNoise:
    def __init__(self, dimension: tuple[int, int], octave: int = 1) -> None:
        self.dimension_x = dimension[0]
        self.dimension_y = dimension[1]
        self.octave = octave

    def random_generated_points(self):
        list_x = []
        matrix_points = []
        for _ in range(self.dimension_y):
            for _ in range(self.dimension_x):
                matrix_random_point_x = random.uniform(0, 1)
                matrix_random_point_y = random.uniform(0, 1)
                point = (matrix_random_point_x, matrix_random_point_y)
                list_x.append(point)
            matrix_points.append(list_x)
        return matrix_points

    def point_vector(self):
        matrix_points = self.random_generated_points()
        # for point in range(len(matrix_points)):
        print(matrix_points)

    def random_generated_vectors(self):
        vetor_len_x = self.dimension_x + 1
        vetor_len_y = self.dimension_y + 1
        list_vector = []
        matrix_vectors = []
        for _ in range(vecto_len_x):
            for _ in range(vector_len_y):
                vector_random_x = random.uniform(0, 1)
                vector_random_y = random.uniform(0, 1)
                vector = (vector_random_x, vector_random_y)
                list_vector.append(vector)
            matrix_vector.append(list_vector)
        return matrix_vector


if __name__ == "__main__":
    dimensions = (2, 2)
    x = PerlinNoise(dimensions, 1)
    x.point_vector()
