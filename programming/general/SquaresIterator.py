class SquaresIterator:
    """
    Class to implement squares upto a given
    max number
    """

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


for i in SquaresIterator(5):
    print(i)
