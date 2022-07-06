class Matrix:
  
  @staticmethod
  def create(x, y): #this method creates a bidimensional array
    return [
        [None for i in range(y)] for i in range(x)
      ]

  @staticmethod
  def define_elements(array, callback): #this method define all elements in a bidimensional array
    for x in range(0, len(array)):
      for y in range(0, len(array[0])):
        array[x][y] = callback(x, y)  

  @staticmethod
  def map(array, callback):
    for x in range(0, len(array)):
      for y in range(0, len(array[0])):
       callback(x, y)  

  @staticmethod
  def get_neighbors(x, y, matrix):
    width = len(matrix)
    height = len(matrix[0])
    neighbors = []

    if(x > 0): neighbors.append(matrix[x - 1][y])
    if(x < width - 1): neighbors.append(matrix[x + 1][y])

    if(y > 0): 
      neighbors.append(matrix[x][y - 1])
      if(x > 0): neighbors.append(matrix[x - 1][y - 1])
      if(x < width - 1): neighbors.append(matrix[x + 1][y - 1])

    if(y < height - 1):
      neighbors.append(matrix[x][y + 1])
      if(x > 0): neighbors.append(matrix[x - 1][y + 1])
      if(x < width - 1): neighbors.append(matrix[x + 1][y + 1])

    return neighbors
