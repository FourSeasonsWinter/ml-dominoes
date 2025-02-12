from classes.game import Game
from classes.player import Player
from screen import *

def main():
  players = [Player(1), Player(2)]
  game = Game(players)

  print_hands(game.players)


main()