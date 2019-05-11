class Xrange:
    '''
        Takes in either 1, 2 or 3 arguments and returns
        a range of values with the last included
    '''

    def __init__(self, *args):
        self.numargs = len(args)
        if self.numargs < 1:
            raise TypeError('Expected ay least 1 argument got 0')
        elif self.numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif self.numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif self.numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError(f'Expected at most 3 arguments got {self.numargs}')

    def __iter__(self):
        while self.start <= self.stop:
            yield self.start
            self.start += self.step

    def __str__(self):
        if self.numargs < 1:
            raise TypeError('Expected ay least 1 argument got 0')
        if self.numargs == 1 or self.numargs == 2:
            return f'Xrange({self.start}, {self.stop})'
        elif self.numargs == 3:
            return f'Xrange({self.start}, {self.stop}, {self.step})'
        else:
            raise TypeError(f'Expected at most 3 arguments got {self.numargs}')


def main():
    list_range = list(Xrange(100, 200, 10))
    print(list_range)


if __name__ == '__main__':
    main()
