class Drob(object):
    """ Дробь вида a/b"""

    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self.normalize()

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        divisor = 2
        while divisor <= min(abs(self.a), abs(self.b)):
            while self.a % divisor == 0 and self.b % divisor == 0:
                self.a //= divisor
                self.b //= divisor
            divisor += 1
        if self.b < 0:
            self.a *= -1
            self.b *= -1

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    def __truediv__(self, other):
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Drob(new_a, new_b)

# Проверка функций
d1 = Drob(1, 2)
d2 = Drob(1, 3)

print(d1 == d1)  # True
print(d1 == d2)  # False
print(d1 < d2)   # False

print(d1 + d2)   # 5/6
print(d1 - d2)   # 1/6
print(d1 * d2)   # 1/6
print(d1 / d2)   # 3/2