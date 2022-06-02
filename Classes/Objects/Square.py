from Classes.Modules.Matrix import Matrix
import pygame

class Square:
  def __init__(self, screen, table, x, y):
    self.sreen = screen
    self.image = pygame.image.load('images/quadmi.png')
    self.table = table
    self.x = x #x and y here are the index in Table.squares[]
    self.y = y

    self.isOpened = False 
    self.isBomb = False
    self.isFlaged = False
    self.neighborsBombs = 0
    self.neighbors = []

    self.draw()

  def draw(self):
    #get (x,y) positions
    x = self.x * 32 + 16
    y = self.y * 32 + 104

    self.sreen.blit(self.image, (x, y))

  def getNeighborsBombs(self):
    self.neighbors = Matrix.getNeighbors(self.x, self.y, self.table)
    filteredNeighbors = filter(lambda neighbor: neighbor.isBomb, self.neighbors)
    self.neighborsBombs = len(list(filteredNeighbors))

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
  def neighbors(self):
    return self.__neighbors
    
  @property
  def neighborsBombs(self):
    return self.__neighborsBombs

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

  @neighbors.setter
  def neighbors(self, value):
    self.__neighbors = value
    
  @neighborsBombs.setter
  def neighborsBombs(self, value):
    self.__neighborsBombs = value




  
