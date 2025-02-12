def print_hands(players):
  for player in players:
    print(f"\nplayer {player.id}:")
  
    for tile in player.hand:
      print(f"{tile.first}|{tile.second}")


def print_tiles(tiles):
  print("remaining tiles:")
  for tile in tiles:
    print(f"{tile.first}|{tile.second}")