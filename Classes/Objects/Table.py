import pygame
import random

from Classes.Game.Text import Text
from Classes.Game.Background import Background
from Classes.Objects.Square import Square
from Classes.Modules.Matrix import Matrix  # Matrix is an own module
from Classes.Modules.Point import Point


class Table:
  def __init__(self, screen):
    self.screen = screen
    self.background = Background(pygame.image.load('images/background.png'), screen)

    self.alive = True
    self.won = False

    self.bombs_number = 60
    self.flags_available = self.bombs_number
    self.squares = Matrix.create(24, 15)  # creates a multidimensional array
    self.squares_sprites = pygame.sprite.Group()

    self.score = Text(self.screen, str(self.flags_available), 'Arial', 34, (230, 0, 0), (398, 47))

    self.generate_table()

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
    # Matrix.define_elements is a static method which defines a certain values for all elements in a matrix
    Matrix.define_elements(self.squares, lambda x, y: Square(self.screen, self, x, y))
    Matrix.map(self.squares, lambda x, y: self.squares_sprites.add(self.squares[x][y]))

  def generate_bombs(self):
    i = 0
    while i < self.bombs_number:
      x = random.randint(0, 23)
      y = random.randint(0, 14)
      # it will set True the attribute is_bomb in the square on the position (x, y)
      if not self.squares[x][y].is_bomb:  # to ensure the code just mark as bomb the squares that aren't are yet.
        self.squares[x][y].is_bomb = True
        i += 1

  def get_neighbors(self):
    for line in self.squares:
      for square in line:
        square.get_neighbors_bombs()

  def open_square(self, square):
    if square.is_flagged:
      return
    if square.is_bomb:
      return self.die(square)

    if square.is_opened:
      if len(square.get_neighbors_flags()) == square.neighbors_bombs > 0:
        square.open_neighbors()
    else:
      square.open()

  def add_flag(self, square):
    if square.is_opened:
      return
    if square.is_flagged:
      self.flags_available += 1
    else:
      if self.flags_available == 0:
        return
      self.flags_available -= 1

    self.score.text = str(self.flags_available)
    square.toggle_flag()

  def win(self):
    for line in self.squares:
      for square in line:
        if not square.is_opened and not square.is_flagged:
          square.toggle_flag()

    self.flags_available = 0
    self.score.text = str(self.flags_available)

    self.won = True
    self.draw()

    win_text_left = Text(self.screen, "You Won!", 'Arial', 34, (255, 255, 255), (160, 55))
    win_text_right = Text(self.screen, "You Won!", 'Arial', 34, (255, 255, 255), (535, 55))

    win_text_left.draw()
    win_text_right.draw()

  def die(self, square_exploded):
    self.alive = False

    for line in self.squares:
      for square in line:
        if square.is_bomb or square.is_flagged:
          square.update()

    square_exploded.explode()

  def actions(self, action, event):
    point = Point(event.pos[0], (event.pos[1]))
    squares = pygame.sprite.spritecollide(point, self.squares_sprites, False)

    if not squares: return

    if action == "add-flag":
      for square in squares:
        self.add_flag(square)

    if action == "open-square":
      for square in squares:
        self.open_square(square)

    self.draw()
    self.check_win()

  def check_win(self):
    closed_squares = 0
    for line in self.squares:
      for square in line:
        if not square.is_opened:
          closed_squares += 1

    if closed_squares == self.bombs_number:
      self.win()
