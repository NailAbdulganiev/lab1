class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        sum = 0
        for i in range(n + 1):
            sum += self.transform(i)
        return sum


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3