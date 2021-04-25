import pygame.draw

import contents.utility.geometry
from contents.utility.constants import *


class Character:
    def __init__(self, board, position, life):
        """
        Creates a character
        :param board: Board
        :param position:
        """
        self.board = board
        self.position = position
        self.life = life

    def heal(self, life):
        """
        Heals the character
        :return: int
        """
        self.life += life
        return self.life


class Soldier(Character):
    def __init__(self, board, position, life=100):
        super().__init__(board, position, life)
        self.draw_coordinates = board.cases[position[1]][position[0]].center
        self.case = self.board.cases[self.position[1]][self.position[0]]
        self.case.occupant = self
        self.case.draw()


    def move(self, direction):
        dx, dy = contents.utility.geometry.get_vectors(direction, self.position)

        if 0 <= self.position[0]+dx < self.board.custom_len()[0] and 0 <= self.position[1]+dy < self.board.custom_len()[1]:
            self.case.occupant = None
            self.case.draw()
            self.position = self.position[0]+dx, self.position[1]+ dy
            self.draw_coordinates = self.board.cases[self.position[1]][self.position[0]].center
            self.case = self.board.cases[self.position[1]][self.position[0]]
            self.case.occupant = self
            self.case.draw()
        else:
            raise ValueError("Déplacement interdit hors de limites de la case")

    def draw(self):
        pygame.draw.circle(self.board.screen, WHITE, self.draw_coordinates, 10)