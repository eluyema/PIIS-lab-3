import chess
from game import Game

print('Hello there! Choose one of available search algorithm\n - negomax\n')

method = input("Enter algorithm name: ")

gameEngine = Game(chess.Board(), method)
gameEngine.start()
