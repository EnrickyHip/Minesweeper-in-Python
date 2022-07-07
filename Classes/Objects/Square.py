from Classes.Modules.Matrix import Matrix
import pygame


class Square(pygame.sprite.Sprite):
  def __init__(self, screen, table, x, y):
    super().__init__()
    self.screen = screen
    self.image = pygame.image.load('images/square-closed.png')
    self.table = table

    self.x = x  # x and y here are the index in Table.squares[]
    self.y = y

    self.rect = self.image.get_rect()
    self.rect.x = self.x * 32 + 16
    self.rect.y = self.y * 32 + 104

    self.is_opened = False
    self.is_bomb = False
    self.is_flagged = False
    self.neighbors_bombs = 0
    self.neighbors = []

    self.exploded = False

  number_images = [
    'images/square-opened.png',
    'images/square1.png',
    'images/square2.png',
    'images/square3.png',
    'images/square4.png',
    'images/square5.png',
    'images/square6.png',
    'images/square7.png',
    'images/square8.png',
  ]

  def open(self):
    if self.is_flagged or self.is_opened:
      return True
    if self.is_bomb:
      self.table.die(self)
      return False

    self.is_opened = True
    if self.neighbors_bombs == 0:
      self.open_neighbors()

    self.update()
    return True

  def open_neighbors(self):
    for neighbor in self.neighbors:
      if not neighbor.open():
        break

  def get_neighbors_bombs(self):
    self.neighbors = Matrix.get_neighbors(self.x, self.y, self.table.squares)
    filtered_neighbors = filter(lambda neighbor: neighbor.is_bomb, self.neighbors)
    self.neighbors_bombs = len(list(filtered_neighbors))

  def get_neighbors_flags(self):
    neighbors_flags = []

    for neighbor in self.neighbors:
      if neighbor.is_flagged:
        neighbors_flags.append(neighbor)

    return neighbors_flags

  def toggle_flag(self):
    self.is_flagged = not self.is_flagged
    self.update()

  # ? it's probably not well done
  def update(self):

    if self.is_opened:
      self.image = pygame.image.load(Square.number_images[self.neighbors_bombs])

    elif not self.table.alive:
      if self.exploded:
        self.image = pygame.image.load('images/square-bomb-explode.png')

      elif self.is_flagged:
        if not self.is_bomb:
          self.image = pygame.image.load('images/square-wrong-flag.png')

      elif self.is_bomb:
        self.image = pygame.image.load('images/square-bomb.png')

    elif self.is_flagged:
      self.image = pygame.image.load('images/square-flag.png')
    else:
      self.image = pygame.image.load('images/square-closed.png')

  def explode(self):
    self.exploded = True
    self.update()
