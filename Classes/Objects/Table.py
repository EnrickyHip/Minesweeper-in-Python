import pygame
from Classes.Game.Background import Background


class Table:
  def __init__(self, screen):
      self.bombNumber = 60
      self.screen = screen
      self.background = Background(pygame.image.load('images/background.png'), screen)

      self.drawTable()

  def drawTable(self):
    self.background.draw()

  def generateBombs(self):
    a = 1
