from Player import HumanPlayer, CPUPlayer
from Board import Board
from copy import deepcopy

def play(board, players):
    current_player = players[0]

    while not board.is_full():
        print()
        for row in board.get_board():
            print(row)

        row, col = current_player.move(deepcopy(board))
        while not board.put(current_player.get_id(), row, col):
            print("Spróbuj jeszcze raz")
            row, col = current_player.move(deepcopy(board))

        current_player.add_points(board.sum_points(row, col))
        current_player = players[0] if current_player == players[1] else players[1]


size = 8
board = Board(size)
players = (HumanPlayer(1, "RED", "Konrad"), CPUPlayer(2, "BLUE"))

play(board, players)
