import math


class Figure:
    def __init__(self, storona_kvadrata=None,
                 radius_kruga=None,
                 storona_romba=None,
                 vysota_romba=None,
                 d1_storona_quadrangle=None,
                 d2_storona_quadrangle=None,
                 a1_storona_triangle=None,
                 a2_storona_triangle=None,
                 a3_storona_triangle=None
                 ):
        self.kvadrat = storona_kvadrata
        self.radius = radius_kruga
        self.lromb = storona_romba
        self.hromb = vysota_romba
        self.d1quad = d1_storona_quadrangle
        self.d2quad = d2_storona_quadrangle
        self.a1tria = a1_storona_triangle
        self.a2tria = a2_storona_triangle
        self.a3tria = a3_storona_triangle


class Square(Figure):
    def perimetr(self):
        return f'perimetr: {4 * self.kvadrat}'

    def area(self):
        return f'ploschad: {self.kvadrat ** 2}'


class Round(Figure):
    def perimetr(self):
        return f'perimetr: {2 * 3.14 * self.radius}'

    def area(self):
        return f'ploschad: {3.14 * (self.radius ** 2)}'


class Rhombus(Figure):
    def perimetr(self):
        return f'perimetr: {4 * self.lromb}'

    def area(self):
        return f'ploschad: {self.lromb * self.hromb}'


class Quadrangle(Figure):
    def perimetr(self):
        return f'perimetr: {self.d1quad * self.d2quad}'

    def area(self):
        return f'ploschad: {self.lromb * self.hromb}'


class Triangle(Figure):
    def perimetr(self):
        return f'perimetr: {self.a1tria + self.a2tria + self.a3tria}'

    def area(self):
        return f'ploschad: {self.lromb * self.hromb}'


fig = Round(radius_kruga=12)
print(fig.area())
