"""

Main file

"""

import sys
import pygame
import contents.board.backboard
import contents.board.menu
import contents.characters.characters

if __name__ == "__main__":
    pygame.init()
    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)
    board_size = board_width, board_height = 1300, 900
    menu_size = menu_width, menu_height = 300, 900
    board = contents.board.backboard.Board(screen, board_width, board_height)
    board.draw_board(20)

    menu = contents.board.menu.Menu(screen, board_width, 0, menu_width, menu_height)
    bouton = contents.board.menu.Button(screen, 1300, 0, 200, 50, "Test")
    menu.add(bouton)
    menu.draw()

    soldat = contents.characters.characters.Soldier(board, (1, 1))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
