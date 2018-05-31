class Stratego:
    def __init__(self, size, player1, player2):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.red_player = player1
        self.blue_player = player2

    def put(self, player, row, col):
        if self.can_put(row, col):
            self.board[row][col] = player.get_id()
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

    def play(self, player):
        for row_p in self.board:
            print(row_p)
        while True:
            print("Ruch gracza:", player.get_name(), "ma punktów:", player.get_points())
            try:
                row, col = int(input("Wiersz:")), int(input("Kolumna:"))
                if self.put(player, row, col):
                    break
                else:
                    print("Wybierz inne miejsce.")
            except:
                print("Zła wartość, jeszcze raz.")

        points = self.count_row(row) + self.count_col(col) + \
                 self.count_diagonal_left(row, col) + self.count_diagonal_right(row, col)

        if points > 0:
            player.add_points(points)
            print("Gratulacje, zdobyłeś", points, "punktów.")

        if player == self.red_player:
            self.play(self.blue_player)
        elif player == self.blue_player:
            self.play(self.red_player)


class HumanPlayer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.points = 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def add_points(self, points):
        self.points += points


player_red = HumanPlayer(1, input("Imie pierwszego gracza:"))
player_blue = HumanPlayer(2, input("Imie drugiego gracza:"))

stratego = Stratego(8, player_red, player_blue)
stratego.play(player_red)
