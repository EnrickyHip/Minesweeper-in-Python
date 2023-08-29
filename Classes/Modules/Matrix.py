from typing import TypeVar, Callable

T = TypeVar('T')

class Matrix():

  @staticmethod
  def create(x: int, y: int, callback: Callable[[int, int], T]) -> list[list[T]]:  # this method creates a matrix
    matrix = [
      [callback(j, i) for i in range(y)] for j in range(x)
    ]

    return matrix

  @staticmethod
  def for_each(array: list[list[T]], callback: Callable[[T], None]):
    for x in range(len(array)):
      for y in range(len(array[0])):
        callback(array[x][y])

  @staticmethod
  def get_neighbors(x: int, y: int, matrix: list[list[T]]) -> list[T]:
    width = len(matrix)
    height = len(matrix[0])
    neighbors: list[T] = []

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
