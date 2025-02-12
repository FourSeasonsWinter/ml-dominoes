from classes.board import Board
from classes.tile import Tile
from classes.player import Player
import random

class Game:
  board = Board()
  round = 0


  def __init__(self, players):
    self.setup(players)


  def setup(self, players):
    self.players = players
    self.tiles = self.__create_tiles()

    random.shuffle(self.tiles)
    self.__deal_tiles(self.players, self.tiles)

    self.current_player = self.__get_first_player(self.players)


  def __create_tiles(self):
    tiles = []

    for first in range(7):
      for second in range(7):
        tile = Tile(first, second)

        if tile in tiles:
          continue

        tiles.append(tile)
    
    return tiles


  def __deal_tiles(self, players, tiles):
    amount_to_deal = 7

    if len(players) == 3:
      amount_to_deal = 9
    elif len(players) == 4:
      amount_to_deal = 6
    
    for player in players:
      for _ in range(amount_to_deal):
        player.add_tile(tiles.pop())


  def __get_first_player(self, players):
    first_player_id = 0
    largest_tile = Tile(0, 0)
    largest_sum = 0

    #get highest double
    for player in players:
      for tile in player.hand:
        sum = tile.first + tile.second
        largest_sum = largest_tile.first + largest_tile.second
        if tile.first == tile.second and sum < largest_sum:
          largest_sum = sum
          first_player_id = player.id
          largest_tile = tile
    
    if largest_sum != 0:
      self.print_starter(first_player_id, largest_tile)
      return first_player_id, largest_tile

    # get highest sum
    for player in players:
      for tile in player.hand:
        sum = tile.first + tile.second
        if sum > largest_sum:
          largest_sum = sum
          first_player_id = player.id
          largest_tile = tile

    self.print_starter(first_player_id, largest_tile)
    return first_player_id, largest_tile
  

  def print_starter(self, id, tile):
    print(f"player {id} with {tile.first}|{tile.second}")
