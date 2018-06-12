from Player import *

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

    def count_points(self, row, col):
        return self.count_row(row) + self.count_col(col) + \
                self.count_diagonal_left(row, col) + self.count_diagonal_right(row, col)

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def play(self, player):
        if self.is_full():
            print("Koniec gry")
            return

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

        points = self.count_points(row, col)

        if points > 0:
            player.add_points(points)
            print("Gratulacje, zdobyłeś", points, "punktów.")

        if player == self.red_player:
            self.play(self.blue_player)
        elif player == self.blue_player:
            self.play(self.red_player)


player_red = Player(1, input("Imie pierwszego gracza:"), 'red')
player_blue = Player(2, input("Imie drugiego gracza:"), 'blue')

stratego = Stratego(8, player_red, player_blue)
stratego.play(player_red)
