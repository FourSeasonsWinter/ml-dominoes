class Tile:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  
  def __eq__(self, value):
    if not isinstance(value, Tile):
      return False
    
    return (self.first == value.first and self.second == value.second) or (self.first == value.second and self.second == value.first)