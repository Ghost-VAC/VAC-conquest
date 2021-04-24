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
