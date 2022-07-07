class Background:
  def __init__(self, background, screen):
    self.background = background
    self.screen = screen

  def draw(self):
    self.screen.blit(self.background, (0, 0))  # it draws the background in the window
