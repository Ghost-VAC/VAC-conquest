import cmath
import math


class Hexagon:
    def __init__(self, center: tuple[int, int], size: int):
        """
        Create an hexagon using its center and its radius
        :param center: tuple[int,int]
        :param size: int
        """
        self.center = center
        self.x, self.y = center
        self.complex_center = int(self.x)+int(self.y)*1j
        self.size = size

    def get_points(self):
        """
        Returns the points of the hexagon
        :return: list[int*6]
        """
        points = []
        for i in range(6):
            complex_point = self.complex_center + cmath.rect(self.size, i*math.pi/3+math.pi/6)
            points.append((complex_point.real, complex_point.imag))
        return points


def get_vectors(direction, position):
    dx = -((position[1] % 2) - 1)
    if direction == "LEFT":
        return -1, 0
    elif direction == "RIGHT":
        return 1, 0
    elif direction == "UL":
        return -1+dx, -1
    elif direction == "UR":
        return 0+dx, -1
    elif direction == "DR":
        return 0+dx, 1
    elif direction == "DL":
        return -1+dx, 1
    else:
        raise ValueError("Unknown direction")