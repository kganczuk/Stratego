class Player():
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