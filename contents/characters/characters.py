import pygame.draw

import contents.utility.geometry
from contents.utility.constants import *

from QtObjects.gamepages.gamepage import GamePage

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
        """
        Creates a soldier
        The basic troop
        :param board: board
        :param position: tuple[int,int]
        :param life: int
        """
        super().__init__(board, position, life)
        self.draw_coordinates = board.cases[position[1]][position[0]].center
        self.case = self.board.cases[self.position[1]][self.position[0]]
        self.case.occupant = self
        self.case.draw()

    def move(self, direction):
        """
        Moves the soldier
        :param direction: str
        :return: case
        """
        dx, dy = contents.utility.geometry.get_vectors(direction, self.position)

        if 0 <= self.position[0]+dx < self.board.dimensions()[0] \
                and 0 <= self.position[1]+dy < self.board.dimensions()[1]:
            self.case.occupant = None
            self.case.draw()
            self.position = self.position[0] + dx, self.position[1] + dy
            self.draw_coordinates = self.board.cases[self.position[1]][self.position[0]].center
            self.case = self.board.cases[self.position[1]][self.position[0]]
            self.case.occupant = self
            self.case.draw()
            print(self.board.screen.window.currentCentralWidget)
            self.board.screen.window.currentCentralWidget = GamePage(self.board.screen, width=300, height=500)
            self.board.screen.window.setCentralWidget(self.board.screen.window.currentCentralWidget)
            print("Hey")
        else:
            raise ValueError("Forbidden move outside of the bord bounds")

        return self.case

    def draw(self):
        """
        Draws the soldier
        :return: None
        """
        pygame.draw.circle(self.board.screen, WHITE, self.draw_coordinates, 10)