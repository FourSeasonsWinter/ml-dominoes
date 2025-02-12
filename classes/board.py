class Board:
  def __init__(self):
    self.board = []

    self.first_tile_value = []
    self.rightmost = []
    self.leftmost = []
  

  def add_first_tile(self, tile):
    self.board.append(tile)

    if tile.first != tile.second:
      self.first_tile_value = [tile.first, tile.second]
      return
    
    self.first_tile_value = tile.first
  

  def add_tile(self, tile, direction):
    # se for na esquerda, o second precisa ter o mesmo valor do leftmost
    if direction == 0:
      if not tile.second == self.leftmost:
        tile.first, tile.second = tile.second, tile.first

      self.board.insert(0, tile)
      self.leftmost = tile.first
    else:
      if not tile.first == self.rightmost:
        tile.first, tile.second = tile.second, tile.first
      
      self.board.append(tile)
      self.rightmost = tile.second
      

