class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_coords(self):
        return ((self.x, self.y))

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __eq__(self, other):
        return self.name == other.name and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self.name == other.name and self.x == other.x and self.y == other.y)

    def __gt__(self, other):
        if self.name > other.name or (self.name == other.name and self.x > other.x) or \
                (self.name == other.name and self.x == other.x and self.y > other.y):
            return True
        return False

    def __lt__(self, other):
        if self.name < other.name or (self.name == other.name and self.x < other.x) or \
                (self.name == other.name and self.x == other.x and self.y < other.y):
            return True
        return False

    def __le__(self, other):
        return not (self > other)

    def __ge__(self, other):
        return not (self < other)