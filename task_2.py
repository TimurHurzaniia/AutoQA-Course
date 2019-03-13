import math


class Rectangle():
    def __init__(self, a_short=1, b_long=2):
        self.a_short = a_short
        self.b_long = b_long

    def get_square(self):
        return self.a_short * self.b_long

    def get_perim(self):
        return 2 * (self.a_short + self.b_long)


class Dot():
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    def zero_dist(self):
        d = (self.X ** 2 + self.Y ** 2) ** 0.5
        return d

    def to_dot_dist(self, dot):
        d = ((self.X - dot.X) ** 2 + (self.Y - dot.Y) ** 2) ** 0.5
        return round(d, 2)

    def polar(self):
        r = (self.X ** 2 + self.Y ** 2) ** 0.5
        if self.Y == 0:
            theta = 180 if self.X < 0 else 0
        elif self.X == 0:
            theta = 90 if self.Y > 0 else 270
        else:
            theta = math.degrees(math.atan(float(self.Y) / self.X))
        return round(r, 2), round(theta, 2)


if __name__ == '__main__':
    dot1 = Dot(-12, 0)
    dot2 = Dot(5, 5)
    print(dot1.zero_dist(), dot1.to_dot_dist(dot2), dot1.polar(), sep='\n')
