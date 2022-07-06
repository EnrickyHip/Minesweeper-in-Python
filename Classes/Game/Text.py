import pygame

class Text:
  def __init__(self, screen, text, font, fontSize, color, position):
    self.screen = screen
    self.color = color
    self.text = text
    self.position = position
    self.font = pygame.font.SysFont(font, fontSize)

  def draw(self):
    render = self.font.render(self.text, True, self.color)
    self.screen.blit(render, self.position)