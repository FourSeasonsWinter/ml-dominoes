class Player:
  hand = []

  def __init__(self, id):
    self.id = id
  
  def add_tile(self, tile):
    self.hand.append(tile)


class Tile:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  
  def __eq__(self, value):
    if not isinstance(value, Tile):
      return False
    
    return (self.first == value.first and self.second == value.second) or (self.first == value.second and self.second == value.first)


def main():
  tiles = []

  for first in range(7):
    for second in range(7):
      tile = Tile(first, second)

      if tile in tiles:
        continue

      tiles.append(tile)
  
  for tile in tiles:
    print(str(tile.first) + " " + str(tile.second))
  
  print("length: " + str(len(tiles)))

main()