import math


class Quadratics:
    def __init__(self, a, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c
        self.discriminant = math.pow(self._b, 2) - (4 * self._a * self._c)
        self.max_or_min_x = - (self._b) / (2 * self._a)
        self.max_or_min_y = - (self.discriminant) / (4 * self._a)

    def roots(self):
        if self.discriminant < 0:
            return f'The roots are complex. Discriminant(D) is negative i.e {self.discriminant}.'
        else:
            root_1 = (-(self._b) + math.sqrt(self.discriminant)) / (2 * self._a)
            root_2 = (-(self._b) - math.sqrt(self.discriminant)) / (2 * self._a)
            rounded_root_1 = round(root_1, 4)
            rounded_root_2 = round(root_2, 4)
            return f'The roots are {rounded_root_1} and {rounded_root_2}.'

    def root_type(self):
        if self.discriminant == 0:
            return "Nature(type) of roots: 'REAL' and 'EQUAL'"
        elif self.discriminant < 0:
            return "Nature(type) of roots: 'COMPLEX' or 'IMAGINARY"
        elif self.discriminant > 0:
            return "Nature(type) of roots: 'REAL' and 'Distinct"
        else:
            return "Nature(type) of roots: 'REAL"

    def get_max_or_min_point(self):
        if self._a < 0:
            if int(self._b) == 0:
                return f'Maximum Point: (0, {self.max_or_min_y})'
            if int(self.discriminant) == 0:
                return f'Maximum Point: ({self.max_or_min_x}, 0)'
            return f'Maximum Point: ({self.max_or_min_x}, {self.max_or_min_y})'
        elif self._a > 0:
            if int(self._b) == 0:
                return f'Minimum Point: (0, {self.max_or_min_y})'
            if int(self.discriminant) == 0:
                return f'Minimum Point: ({self.max_or_min_x}, 0)'
            return f'Minimum Point: ({self.max_or_min_x}, {self.max_or_min_y})'

    def get_line_of_symmetry(self):
        return f'Line of symmetry: x = {self.max_or_min_x}'

    def get_discriminant(self):
        return f'D = {self.discriminant}'
