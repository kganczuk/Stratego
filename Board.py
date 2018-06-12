class Board:
    def __init__(self, size):
        self.size = size
        self.board = create_board(size)

    def put(self, player_id, row, col):
        if self.can_put(row, col):
            self.board[row][col] = player_id
            return True
        else:
            return False

    def can_put(self, row, col):
        if row in range(self.size) and col in range(self.size):
            return self.board[row][col] == 0
        else:
            return False

    def count_row(self, row):
        points = 0
        for col in range(self.size):
            if self.board[row][col] == 0:
                return 0
            else:
                points += 1

        return points

    def count_col(self, col):
        points = 0
        for row in range(self.size):
            if self.board[row][col] == 0:
                return 0
            else:
                points += 1

        return points

    def count_diagonal_right(self, row, col):
        points = 0
        ix, iy = row-1, col-1
        while ix >= 0 and iy >= 0:
            if self.board[ix][iy] == 0:
                return 0
            else:
                points += 1
            ix -= 1
            iy -= 1

        ix, iy = row+1, col+1
        while ix < self.size and iy < self.size:
            if self.board[ix][iy] == 0:
                return 0
            else:
                points += 1
            ix += 1
            iy += 1

        if points > 0:
            return points+1
        else:
            return 0

    def count_diagonal_left(self, row, col):
        points = 0
        ix, iy = row+1, col-1
        while ix < self.size and iy >= 0:
            if self.board[ix][iy] == 0:
                return 0
            ix += 1
            iy -= 1

        ix, iy = row-1, col+1
        while ix >= 0 and iy < self.size:
            if self.board[ix][iy] == 0:
                return 0
            else:
                points += 1
            ix -= 1
            iy += 1

        if points > 0:
            return points+1
        else:
            return 0

    def sum_points(self, row, col):
        return self.count_row(row) + self.count_col(col) + \
                self.count_diagonal_left(row, col) + self.count_diagonal_right(row, col)

    def is_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def get_board(self):
        return self.board


def create_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]