import cmath
import math

class Hexagon():
    def __init__(self, center:tuple[float,float], size:int):
        self.center = center
        self.x, self.y = center
        self.complex_center = int(self.x)+int(self.y)*1j
        self.size = size

    def get_points(self):
        points = []
        for i in range(6):
            complexpoint = self.complex_center + cmath.rect(self.size, i*math.pi/3+math.pi/6)
            points.append((complexpoint.real, complexpoint.imag))
        return points
