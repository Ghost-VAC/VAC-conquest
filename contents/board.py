import pygame
import math
import contents.utility.geometry

class Plateau():
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def draw_plateau(self):
        R = 20
        m=1

        for y in range(1,self.height//int(math.sqrt(3)*R)+2):
            for x in range(1,self.width//int(math.sqrt(3)*R)-1):
                offset = (y % 2 == 0) * math.sqrt(3) * (R / 2)

                points = contents.utility.geometry.Hexagon((math.sqrt(3)*R*x+offset,3/2*R*y), R).get_points()
                pygame.draw.polygon(self.screen, pygame.Color(255,255,255),points,width=m)

