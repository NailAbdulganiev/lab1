class Summator:

    def transform(self, n):
        return n

    def sum(self, n):
        sum = 0
        for i in range(n + 1):
            sum += self.transform(i)
        return sum


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        self.b = 2


class CubeSummator(PowerSummator):
    def __init__(self):
        self.b = 3


r = CubeSummator()
print(r.sum(3))
