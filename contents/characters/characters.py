import pygame.draw

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
        self.draw_coordinates = board.cases[position[0]][position[1]].center

        pygame.draw.circle(board.screen,WHITE,self.draw_coordinates,10)

    def move(self,dx, dy):
        print(self.board.custom_len())

        if 0 <= self.position[0]+dx < self.board.custom_len()[0] and 0 <= self.position[1]+dy < self.board.custom_len()[1]:
            self.position = self.position + (dx,dy)