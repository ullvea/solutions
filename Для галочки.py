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


class CheckMark:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a.name}{self.b.name}{self.c.name}"

    def __bool__(self):
        return (self.a.x - self.c.x) * (self.b.y - self.c.y) - (self.b.x - self.c.x) * (self.a.y - self.c.y) != 0

    def __eq__(self, other):
        return (self.b.x == other.b.x and self.b.y == other.b.y and self.a.x == other.a.x and self.a.y == other.a.y and
                self.c.x == other.c.x and other.c.y == self.c.y) or (
                self.b.x == other.b.x and self.b.y == other.b.y and self.c.x == other.a.x and self.c.y == other.a.y
                and self.a.x == other.c.x and other.a.y == self.c.y)
