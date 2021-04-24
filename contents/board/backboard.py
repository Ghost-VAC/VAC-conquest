import pygame
import math
import contents.utility.geometry


class Board:

    def __init__(self, screen, width, height):
        """
        Initilialization of the game board.
        :param screen: pygame.Surface
        :param width: int
        :param height: int
        :param case_radius: int
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.cases = []


    def draw_board(self, radius, stroke_width=1):
        """
        Draws the board on the screen
        :param radius: Radius of the hexagon
        :param stroke_width: Stroke width
        :return: None
        """

        def fy(y):
            """
            Returns the formula for y points
            :param y:
            :return: int
            """
            return y * 3 * radius // 2

        def fx(x):
            """
            Returns the formula for x points
            :param x: int
            :return: int
            """
            return int(x * math.sqrt(3) * radius)

        if self.cases:
            raise ValueError("Board is not empty")

        max_y = self.height // fy(1) - 1
        max_x = self.width // fx(1) - 2
        y_zero = fy(1)
        x_zero = fx(1)

        for y in range(max_y):
            self.cases.append([])
            for x in range(max_x):
                offset = (y % 2 == 0) * math.sqrt(3) * (radius / 2)
                center_x = int(fx(x) + offset) + x_zero
                center_y = fy(y) + y_zero
                self.cases[y].append(Case((center_x,center_y),radius))
                #points = contents.utility.geometry.Hexagon((center_x, center_y), radius).get_points()
                #pygame.draw.polygon(self.screen, pygame.Color(255, 255, 255), points, width=stroke_width)

                pygame.draw.polygon(self.screen,pygame.Color(255,255,255),self.cases[y][x].hexagon.get_points(), width=stroke_width)


class Case:
    def __init__(self, center, size, type = None, occupant = None):
        """
        Case class, made for describing the cases of the board
        :param center: tuple[int,int]
        :param size: int
        :param type:
        :param occupant:
        """
        self.center = center
        self.size = size
        self.type = type
        self.occupant = occupant
        self.hexagon = contents.utility.geometry.Hexagon(self.center, self.size)