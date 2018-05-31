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

    def play(self, player):
        for row_p in self.board:
            print(row_p)
        while True:
            print("Ruch gracza:", player.get_name())
            row, col = input("Wiersz:"), input("Kolumna:")
            try:
                if self.put(player, int(row), int(col)):
                    break
                else:
                    print("Wybierz inne miejsce.")
            except:
                print("Zła wartość, jeszcze raz.")

        if player == self.red_player:
            self.play(self.blue_player)
        elif player == self.blue_player:
            self.play(self.red_player)


class HumanPlayer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


player_red = HumanPlayer(1, input("Imie pierwszego gracza:"))
player_blue = HumanPlayer(2, input("Imie drugiego gracza:"))

stratego = Stratego(8, player_red, player_blue)
stratego.play(player_red)
