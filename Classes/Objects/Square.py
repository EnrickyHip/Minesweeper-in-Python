from Classes.Modules.Matrix import Matrix
import pygame

class Square(pygame.sprite.Sprite):
  def __init__(self, screen, table, x, y):
    super().__init__()
    self.sreen = screen
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

    #self.draw()

  def draw(self):
    #get (x,y) positions

    self.sreen.blit(self.image, (self.rect.x,  self.rect.y))

  def get_neighbors_bombs(self):
    self.neighbors = Matrix.get_neighbors(self.x, self.y, self.table)
    filtered_neighbors = filter(lambda neighbor: neighbor.is_bomb, self.neighbors)
    self.neighbors_bombs = len(list(filtered_neighbors))

  #properties 

  @property
  def is_opened(self):
    return self.__is_opened
  
  @property
  def is_bomb(self):
    return self.__is_bomb
  
  @property
  def is_flaged(self):
    return self.__is_flaged 

  @property
  def neighbors(self):
    return self.__neighbors
    
  @property
  def neighbors_bombs(self):
    return self.neighbors_bombs

  #setters 

  @is_opened.setter
  def is_opened(self, value):
    self.__is_opened = value
  
  @is_bomb.setter
  def is_bomb(self, value):
    self.__is_bomb = value
  
  @is_flaged.setter
  def is_flaged(self, value):
    self.__is_flaged = value

  @neighbors.setter
  def neighbors(self, value):
    self.__neighbors = value
    
  @neighbors_bombs.setter
  def neighbors_bombs(self, value):
    self.__neighbors_bombs = value




  
