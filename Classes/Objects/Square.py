import pygame

class Square:
  def __init__(self, screen, x, y):
    self.sreen = screen
    self.image = pygame.image.load('images/quadmi.png')
    self.x = x #x and y here are the index in Table.squares[]
    self.y = y

    self.opened = False 
    self.isBomb = False
    self.neighborBombs = 0

    self.draw()

  def draw(self):
    #get (x,y) positions
    x = self.x * 32 + 16
    y = self.y * 32 + 104

    self.sreen.blit(self.image, (x, y))
