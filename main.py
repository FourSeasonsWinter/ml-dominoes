import random

class Player:
  def __init__(self, id):
    self.id = id
    self.hand = []
  
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
  tiles = create_tiles()
  random.shuffle(tiles)

  player1 = Player(1)
  player2 = Player(2)
  players = [player1, player2]
  deal_tiles(players, tiles)

  print("player 1:")
  for tile in player1.hand:
    print(f"{tile.first}|{tile.second}")

  print("\nplayer 2:")
  
  for tile in player2.hand:
    print(f"{tile.first}|{tile.second}")



def create_tiles():
  tiles = []

  for first in range(7):
    for second in range(7):
      tile = Tile(first, second)

      if tile in tiles:
        continue

      tiles.append(tile)
  
  return tiles


def deal_tiles(players, tiles):
  amount_to_deal = 7

  if len(players) == 3:
    amount_to_deal = 9
  
  for player in players:
    for _ in range(amount_to_deal):
      player.add_tile(tiles.pop())


main()