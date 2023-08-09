import random


class Line:
    def __init__(self, a, b, c, d) -> None:
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d) -> None:
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d) -> None:
        self.sp = (a, b)
        self.ep = (c, d)


figure = [Line, Rect, Ellipse]

elements = [random.choice(figure)(random.randint(1, 100),
                                  random.randint(1, 100),
                                  random.randint(1, 100),
                                  random.randint(1, 100))
            for i in range(217)]

for object in elements:
    if object.__class__.__name__ == 'Line':
        object.sp = (0, 0)
        object.ep = (0, 0)
