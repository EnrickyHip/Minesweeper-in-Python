class MultiArray:
  
  @staticmethod
  def createMultiArray(x, y): #this method creates a multidimensional array
    return [
        [None for i in range(y)] for i in range(x)
      ]

  @staticmethod
  def defineElements(array, callback): #this method define all elements in a multidimensional array
    for x in range(0, 24):
      for y in range(0, 15):
        array[x][y] = callback(x, y)   