import pygame
import contents.board.backboard
import contents.board.menu
import contents.characters.characters


class PygameWindow(pygame.Surface):
    def __init__(self, size):
        super(PygameWindow, self).__init__(size)
        self.size = self.width, self.height = 1600, 900
        self.board_size = self.board_width, self.board_height = 1300, 900
        self.board = contents.board.backboard.Board(self, self.board_width, self.board_height)
        self.board.draw_board(20)

        self.soldat = contents.characters.characters.Soldier(self.board, (1, 1))

    def update(self):
        pass