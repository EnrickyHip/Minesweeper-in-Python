from typing import TypeVar, Callable

T = TypeVar('T')

class Matrix:

  @staticmethod
  def create(x: int, y: int):  # this method creates a matrix
    return [
      [None for i in range(y)] for i in range(x)
    ]

  @staticmethod
  def define_elements(array: list[list[T]], callback: Callable[[int, int], T]):  # this method define all elements in a matrix
    for x in range(len(array)):
      for y in range(len(array[0])):
        array[x][y] = callback(x, y)

  @staticmethod
  def for_each(array: list[list[T]], callback: Callable[[int, int], None]):
    for x in range(len(array)):
      for y in range(len(array[0])):
        callback(array[x][y])

  @staticmethod
  def get_neighbors(x: int, y: int, matrix: list[list[T]]):
    width = len(matrix)
    height = len(matrix[0])
    neighbors = []

    if x > 0:
      neighbors.append(matrix[x - 1][y])
    if x < width - 1:
      neighbors.append(matrix[x + 1][y])

    if y > 0:
      neighbors.append(matrix[x][y - 1])
      if x > 0:
        neighbors.append(matrix[x - 1][y - 1])
      if x < width - 1:
        neighbors.append(matrix[x + 1][y - 1])

    if y < height - 1:
      neighbors.append(matrix[x][y + 1])
      if x > 0:
        neighbors.append(matrix[x - 1][y + 1])
      if x < width - 1:
        neighbors.append(matrix[x + 1][y + 1])

    return neighbors
