import pygame
import random

from Classes.Game.Text import Text
from Classes.Game.Background import Background
from Classes.Objects.Square import Square
from Classes.Modules.Matrix import Matrix #Matrix is an own module 
from Classes.Modules.Point import Point

class Table:
  def __init__(self, screen):
      self.screen = screen
      self.background = Background(pygame.image.load('images/background.png'), screen)

      self.bombs_number = 60
      self.flags_available = self.bombs_number
      self.squares = Matrix.create(24, 15) #creates a multidimensional array
      self.squares_sprites = pygame.sprite.Group()

      self.score = Text(self.screen, str(self.flags_available), 'Arial', 34, (230, 0, 0), (398, 47))

      self.generate_table()

      # for line in self.squares:
      #   print ('  '.join(map(str, [square.is_bomb for square in line])))
      
      # for line in self.squares:
      #   print ('  '.join(map(str, [square.neighbors_bombs for square in line])))

  def generate_table(self):    
    self.generate_squares()
    self.generate_bombs()
    self.get_neighbors()

    self.draw()
  
  def draw(self):
    self.background.draw()
    self.score.draw()
    self.squares_sprites.draw(self.screen)
  
  def generate_squares(self):
    #Matrix.define_elements is a static method which defines a certain values for all elements in a multidimensionalArray
    Matrix.define_elements(self.squares, lambda x, y: Square(self.screen, self, x, y))
    Matrix.map(self.squares, lambda x, y: self.squares_sprites.add(self.squares[x][y]))        

  def generate_bombs(self):
    i = 0
    while i < self.bombs_number:
      x = random.randint(0, 23)
      y = random.randint(0, 14)
      #it will set True the attribute is_bomb in the square on the position (x, y)
      if not (self.squares[x][y].is_bomb): #to ensure the code just mark as bomb the squares that isn't are yet.
        self.squares[x][y].is_bomb = True
        i += 1
  
  def get_neighbors(self):
    for x in range(0, len(self.squares)):
      for y in range(0, len(self.squares[0])):
        self.squares[x][y].get_neighbors_bombs()

  def open_square(self, square):
    if (square.is_flaged): return
    if (square.is_bomb): return self.die()

    if (square.is_opened):
      if (len(square.get_neighbors_flags()) == square.neighbors_bombs > 0):
        square.open_neighbors()
    else:
      square.open()

  def add_flag(self, square):
    if (square.is_opened): return
    if (square.is_flaged):
      self.flags_available += 1
    else:
      if (self.flags_available == 0): return
      self.flags_available -= 1
      
    self.score.text = str(self.flags_available)
    square.toggle_flag()
  
  def die(self):
    print("morreu")

  def actions(self, action, event):
    point = Point(event.pos[0], (event.pos[1]))
    squares = pygame.sprite.spritecollide(point, self.squares_sprites, False)

    if not(squares): return

    if (action == "add-flag"):
      for square in squares:
        self.add_flag(square)
    
    if (action == "open-square"):
      for square in squares:
        self.open_square(square)
        
    self.draw()


    
        





