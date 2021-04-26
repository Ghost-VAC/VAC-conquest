from PySide6.QtWidgets import *
import contents.Build.QtBuild
import sys

import pygame
import contents.board.backboard
import contents.board.menu
import contents.characters.characters


class Game(QWidget):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Click me")
        w = contents.Build.QtBuild.MainWindow(screen)

        # Create layout and add widgets
        game_layout = QLayout()
        menu_layout = QVBoxLayout()
        menu_layout.setSizeConstraint(menu_layout.SetMaximumSize)
        game_layout.addWidget(w)
        menu_layout.addWidget(self.edit)
        menu_layout.addWidget(self.button)
        game_layout.addLayout(menu_layout)

        # Set dialog layout
        self.setLayout(game_layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

        # Greets the user

    def greetings(self):
        print(f"Hello {self.edit.text()}")


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1300, 900
    screen = pygame.Surface(size)
    board_size = board_width, board_height = 1300, 900
    menu_size = menu_width, menu_height = 300, 900
    board = contents.board.backboard.Board(screen, board_width, board_height)
    board.draw_board(20)

    #menu = contents.board.menu.Menu(screen, board_width, 0, menu_width, menu_height)
    #button = contents.board.menu.Button(screen, 1300, 0, 200, 50, "Test")
    #menu.add(button)
    #menu.draw()

    def say_hello():
        print("Hello !")

    soldat = contents.characters.characters.Soldier(board, (1, 1))

    app = QApplication(sys.argv)

    game = Game()
    game.show()

    sys.exit(app.exec_())

