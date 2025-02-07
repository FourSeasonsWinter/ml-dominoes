import random
import screen
from player import Player
from tile import Tile


def main():
  tiles = create_tiles()
  random.shuffle(tiles)

  players = [Player(1), Player(2), Player(3), Player(4)]
  deal_tiles(players, tiles)

  first_player = get_first_player(players)
  screen.print_remaining_tiles(tiles)


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
  elif len(players) == 4:
    amount_to_deal = 6
  
  for player in players:
    for _ in range(amount_to_deal):
      player.add_tile(tiles.pop())


def get_first_player(players):
  first_player_id = 0
  largest_sum = 0

  for player in players:
    for tile in player.hand:
      sum = tile.first + tile.second
      if sum > largest_sum:
        largest_sum = sum
        first_player_id = player.id

  return first_player_id


main()