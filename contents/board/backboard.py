import math
import contents.utility.geometry
from contents.utility.constants import *


class Board:
    def __init__(self, screen, width, height):
        """
        Initialization of the game board.
        :param screen: pygame.Surface
        :param width: int
        :param height: int
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

        def fy(ordinate):
            """
            Returns the formula for y points
            :param ordinate:
            :return: int
            """
            return ordinate * 3 * radius // 2

        def fx(abscissa):
            """
            Returns the formula for x points
            :param abscissa: int
            :return: int
            """
            return int(abscissa * math.sqrt(3) * radius)

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
                self.cases[y].append(Case((center_x, center_y), radius))

                pygame.draw.polygon(self.screen, WHITE, self.cases[y][x].hexagon.get_points(), width=stroke_width)


class Case:
    def __init__(self, center, size, kind=None, occupant=None):
        """
        Case class, made for describing the cases of the board
        :param center: tuple[int,int]
        :param size: int
        :param kind:
        :param occupant:
        """
        self.center = center
        self.size = size
        self.kind = kind
        self.occupant = occupant
        self.hexagon = contents.utility.geometry.Hexagon(self.center, self.size)

    def __eq__(self, other):
        """
        Defines the equality of two cases
        :param other: contents.board.backboard.Case
        :return: Bool
        """
        if type(other) != Case:
            raise ValueError("Can only compare a case to another")
        return self.center == other.center

    def __str__(self):
        return str(self.center)+" : "+str(self.kind) + ", " + str(self.occupant)

    def __repr__(self):
        return str(self.center)+" : "+str(self.kind) + ", " + str(self.occupant)