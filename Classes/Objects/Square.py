import pygame

class Square:
  def __init__(self, screen, x, y):
    self.sreen = screen
    self.image = pygame.image.load('images/quadmi.png')
    self.x = x #x and y here are the index in Table.squares[]
    self.y = y

    self.isOpened = False 
    self.isBomb = False
    self.isFlaged = False
    self.neighborBombs = 0

    self.draw()

  def draw(self):
    #get (x,y) positions
    x = self.x * 32 + 16
    y = self.y * 32 + 104

    self.sreen.blit(self.image, (x, y))
   
  #properties 

  @property
  def isOpened(self):
    return self.__isOpened
  
  @property
  def isBomb(self):
    return self.__isBomb
  
  @property
  def isFlaged(self):
    return self.__isFlaged
  
  @property
  def neighborBombs(self):
    return self.__neighborBombs

  #setters 

  @isOpened.setter
  def isOpened(self, value):
    self.__isOpened = value
  
  @isBomb.setter
  def isBomb(self, value):
    self.__isBomb = value
  
  @isFlaged.setter
  def isFlaged(self, value):
    self.__isFlaged = value
  
  @neighborBombs.setter
  def neighborBombs(self, value):
    self.__neighborBombs = value


  
