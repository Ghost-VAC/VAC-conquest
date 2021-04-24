import pygame
import contents.utility.geometry

class Plateau():
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def draw(self):
        points = contents.utility.geometry.Hexagon((100,100), 10).get_points()
        Polygone = pygame.draw.polygon(self.screen, pygame.Color(255,255,255),points,width=1)
