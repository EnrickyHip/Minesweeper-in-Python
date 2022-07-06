from Classes.Modules.Matrix import Matrix
import pygame

class Square(pygame.sprite.Sprite):
  def __init__(self, screen, table, x, y):
    super().__init__()
    self.screen = screen
    self.image = pygame.image.load('images/quadmi.png')
    self.table = table

    self.x = x #x and y here are the index in Table.squares[]
    self.y = y

    self.rect = self.image.get_rect()
    self.rect.x = self.x * 32 + 16
    self.rect.y = self.y * 32 + 104

    self.is_opened = False 
    self.is_bomb = False
    self.is_flaged = False
    self.neighbors_bombs = 0
    self.neighbors = []

  def get_neighbors_bombs(self):
    self.neighbors = Matrix.get_neighbors(self.x, self.y, self.table.squares)
    filtered_neighbors = filter(lambda neighbor: neighbor.is_bomb, self.neighbors)
    self.neighbors_bombs = len(list(filtered_neighbors))

  def set_image(self):
    if (self.is_flaged):
      self.image = pygame.image.load('images/quadban.png')
    else:
      self.image = pygame.image.load('images/quadmi.png')

  def toggle_flag(self):
    self.is_flaged = not self.is_flaged
    self.set_image()



  
