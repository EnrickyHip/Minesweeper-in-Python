from pygame import Surface


class Background:
    def __init__(self, background: Surface, screen: Surface):
        self.background = background
        self.screen = screen

    def draw(self):
        # it draws the background in the window
        self.screen.blit(self.background, (0, 0))
