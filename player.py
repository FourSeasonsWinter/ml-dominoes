class Player:
  def __init__(self, id):
    self.id = id
    self.hand = []
  
  def add_tile(self, tile):
    self.hand.append(tile)