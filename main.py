"""

Main file

"""

import sys
import pygame
import contents.board.backboard
import contents.characters.characters

if __name__ == "__main__":
    pygame.init()
    size = width, height = 960, 720
    screen = pygame.display.set_mode(size)

    board = contents.board.backboard.Board(screen, width, height)
    board.draw_board(20)

    soldat = contents.characters.characters.Soldier(board, (20, 10))

    pygame.display.flip()

    soldat.move(20,-2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
