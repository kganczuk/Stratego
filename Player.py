from copy import deepcopy


class HumanPlayer:
    def __init__(self, id, color, name):
        self.id = id
        self.name = name
        self.color = color
        self.points = 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def add_points(self, points):
        self.points += points

    def get_color(self):
        return self.color

    def print_move(self):
        print("Ruch gracza: ", self.get_name(), "\nPunktów:", self.get_points())

    def move(self, board, players):
        self.print_move()
        try:
            row, col = int(input("Podaj wiersz:")), int(input("Podaj kolumne:"))
        except:
            return -1, -1
        return row, col


class CPUPlayer(HumanPlayer):
    def __init__(self, id, color, name="CPU"):
        self.id = id
        self.name = name
        self.color = color
        self.points = 0

    def move(self, board, players):
        self.print_move()
        points, move = min_max(board, self, self, players)
        print(points, move)
        return move


def min_max(board, player_move, player, players, depth=0):
    temp_board = deepcopy(board)
    next_player = players[0] if player == players[1] else players[1]
    if temp_board.is_full():
        if player == player_move:
            return depth - 10, (-1, -1)
        else:
            return 10 - depth, (-1, -1)
    depth += 1
    result_list = []
    possible_moves_count = sum(temp_board.get_board(), []).count(0)
    if possible_moves_count is 0:
        return 0, (-1, -1)
    possible_moves = []
    for r in range(temp_board.get_size()):
        for c in range(temp_board.get_size()):
            if temp_board.get_field(r, c) is 0:
                possible_moves.append((r, c))
    for r, c in possible_moves:
        temp_board.put(player, r, c)
        ret, (row, col) = min_max(temp_board, player_move, next_player, players, depth)
        result_list.append(ret)
        temp_board.clear_field(row, col)
    if player == player_move:
        max_element = max(result_list)
        return max_element, possible_moves[result_list.index(max_element)]
    else:
        min_element = min(result_list)
        return min_element, possible_moves[result_list.index(min_element)]
