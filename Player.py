class HumanPlayer:
    def __init__(self, id, name, color):
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

    def move(self, board):
        print("Gracz nr", self.get_id(), ", Punktów:", self.get_points())
        try:
            row, col = int(input("Podaj wiersz:")), int(input("Podaj kolumne:"))
        except:
            return -1, -1
        return row, col


class CPUPlayer(HumanPlayer):
    def move(self, board):
        return 0, 0
