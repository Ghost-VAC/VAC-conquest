import pygame.draw
from contents.utility.constants import *


class Menu:
    def __init__(self, screen, x, y, width, height):
        """
        Defines the menu pannel
        :param screen:
        :param width: int
        :param height: int
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.contents = []

    def draw(self):
        delta = 20
        y = self.y + delta
        for content in self.contents:
            x_draw = self.x + (self.width - content.width)/2
            content.draw(x_draw, y)
            y += content.height + delta

    def add(self, content):
        self.contents.append(content)


class MenuObject:
    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Button(MenuObject):
    def __init__(self, screen, x, y, width, height, text):
        super().__init__(screen, x, y, width, height)
        self.text = Text(screen, x, y, width, height, text)

    def draw(self, x, y):
        print([x, y, self.width, self.height])
        pygame.draw.rect(self.screen, WHITE, [x, y, self.width, self.height], width=2)
        self.text.draw()


class Text(MenuObject):
    def __init__(self, screen, x, y, width, height, text, color = WHITE, font = "freesansbold.ttf", size = 24):
        super().__init__(screen, x, y, width, height)
        self.text = text
        self.font = font
        self.font_size = size
        self.color = color
        self.my_font = pygame.font.SysFont(self.font, self.font_size)
        self.text_surface = self.my_font.render(self.text, False, self.color)
        self.text_X = None
        self.text_Y = None
        self.position = self.center
        self.position()

    def center(self):
        self.text_X = (self.width - self.text_surface.get_width())//2 + self.x
        self.text_Y = (self.height - self.text_surface.get_height())//2 + self.y
        self.position = self.center

    def align_right(self):
        self.text_X = self.x
        self.text_Y = self.y
        self.position = self.align_right

    def align_left(self):
        self.text_X = self.width - self.text_surface.get_width() + self.x
        self.text_Y = self.height - self.text_surface.get_height() + self.y
        self.position = self.align_left

    def update_text(self,new_text):
        global need_update
        self.text = new_text
        self.text_surface = self.my_font.render(self.text, False, self.color)
        self.position()
        need_update = True

    def draw(self):
        self.screen.blit(self.text_surface, (self.text_X, self.text_Y))