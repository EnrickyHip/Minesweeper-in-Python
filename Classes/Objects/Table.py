import pygame
import random

from Classes.Game.Background import Background
from Classes.Objects.Square import Square
from Classes.Other.createMultiArray import MultiArray #MultiArray is a own modulek

class Table:
  def __init__(self, screen):
      self.bombsNumber = 60
      self.screen = screen
      self.squares = MultiArray.createMultiArray(24, 15) #creates a multidimensional array
      self.background = Background(pygame.image.load('images/background.png'), screen)

      self.drawTable()

  def drawTable(self):
    self.background.draw()
    self.generateSquares()
    self.generateBombs()
  
  def generateSquares(self):
    #MultiArray.defineElements is a static method which defines a certain values for all elements in a multidimensionalArray
    MultiArray.defineElements( 
        self.squares, 
        lambda x, y: Square(self.screen, x, y) #lambda is an annonymous function 
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
        





