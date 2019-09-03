import pygame
from PyCleanUI.Style import STYLE

class Text:
    def __init__(self, text=""):
        self.text = text
        self.color = STYLE["font"]["color"]

    """ setup everything to render """
    def setup_render(self, window, position):
        self.window = window
        self.position = position
        self.pg_text = self.font.render(self.text, True, self.color)

    """ render every frame """
    def render(self):
        self.window.display.blit(self.get_render(), self.position)

    """ set widget font """
    def set_font(self, font):
        self.font = font

    """ return geometry"""
    def get_size(self):
        return self.pg_text.get_size()

    """ return render -> pygame surface"""
    def get_render(self):
        return self.pg_text
