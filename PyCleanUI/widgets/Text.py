import pygame

class Text:
    def __init__(self, text=""):
        self.text = text

    """ setup everything to render """
    def setup_render(self, window, position):
        self.window = window
        self.color = window.style["font"]["color"]
        self.position = position
        self.pg_text = self.font.render(self.text, True, self.color)

    """ render every frame """
    def render(self):
        self.window.display.blit(self.get_render(), self.position)

    """ setters """
    # set font
    def set_font(self, font):
        self.font = font

    """ getters """
    # return widget px size
    def get_size(self):
        return self.pg_text.get_size()

    # return render -> pygame surface
    def get_render(self):
        return self.pg_text
