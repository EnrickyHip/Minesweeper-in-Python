import pygame
import random

from Classes.Game.Text import Text
from Classes.Game.Background import Background
from Classes.Objects.Square import Square
from Classes.Modules.Matrix import Matrix #MultiArray is a own module

class Table:
  def __init__(self, screen):
      self.screen = screen
      self.background = Background(pygame.image.load('images/background.png'), screen)

      self.bombsNumber = 60
      self.flagsAvailable = self.bombsNumber
      self.squares = Matrix.create(24, 15) #creates a multidimensional array

      self.score = Text(self.screen, str(self.flagsAvailable), 'Arial', 34, (230, 0, 0), (398, 47))

      self.generateTable()

      for line in self.squares:
        print ('  '.join(map(str, [square.isBomb for square in line])))
      
      for line in self.squares:
        print ('  '.join(map(str, [square.neighborsBombs for square in line])))

  def generateTable(self):
    self.background.draw()
    self.score.draw()
    self.generateSquares()
    self.generateBombs()
    self.getNeighbors()
  
  def generateSquares(self):
    #Matrix.defineElements is a static method which defines a certain values for all elements in a multidimensionalArray
    Matrix.defineElements( 
        self.squares,
        lambda x, y: Square(self.screen, self.squares, x, y) #lambda is an annonymous function 
      )        

  def generateBombs(self):
    i = 0
    while i < self.bombsNumber:
      x = random.randint(0, 23)
      y = random.randint(0, 14)
      #it will set True the attribute isBomb in the square on the position (x, y)
      if not (self.squares[x][y].isBomb): #to ensure the code just mark as bomb the squares that isn't are yet.
        self.squares[x][y].isBomb = True
        i += 1
  
  def getNeighbors(self):
    for x in range(0, len(self.squares)):
      for y in range(0, len(self.squares[0])):
        self.squares[x][y].getNeighborsBombs()
    
        





