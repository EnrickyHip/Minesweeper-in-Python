import pygame

from Classes.Objects.Table import Table

class Game:
  def __init__(self):
      pygame.init()

      self.screen = pygame.display.set_mode((800, 600))
      self.icon = pygame.image.load('images/icon.png')
      self.Table = Table(self.screen)

      pygame.display.set_caption("Minesweeper in Python")
      pygame.display.set_icon(self.icon)

      self.loop()
  
  def loop(self):
    clock = pygame.time.Clock()
    window = True
    
    while window:
      clock.tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False

      pygame.display.update()
    pygame.quit()