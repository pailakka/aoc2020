import time

input = '6,4,12,1,20,0,16'

numbers = list(map(int, input.split(',')))


class game:
    def __init__(self, numbers):
        self.numbers = numbers
        self.last_spoken = None
        self.spoken = {}
        self.i = 0
        self.next = None

    def __iter__(self):
        return self

    def speak(self, number):
        self.last_spoken = number
        if number not in self.spoken:
            self.spoken[number] = [self.i, ]
        else:
            self.spoken[number].append(self.i)
            self.spoken[number] = self.spoken[number][-2:]
        # print(self.i, 'speak', number, self.spoken)
        self.i += 1

        self.next = self.resolve_next()
        return number

    def __next__(self):
        n = self.numbers[self.i % len(self.numbers)]
        if self.next is None:
            return self.speak(n)
        else:
            return self.speak(self.next)

    def resolve_next(self):
        n = self.numbers[self.i % len(self.numbers)]
        # print(self.i, 'resolve_next', n, self.last_spoken, self.spoken)
        if n not in self.spoken:
            # print(self.i, 'I')
            return n
        else:
            if len(self.spoken[self.last_spoken]) == 1:
                # print(self.i, 'W')
                return 0
            else:
                # print(self.i, 'N')
                ls = self.spoken[self.last_spoken]
                return ls[1] - ls[0]


g = game(numbers)

st = time.time()
for i in range(30000000 - 1):
    if i % 10e6 == 0:
        print(i, time.time() - st)
        st = time.time()
    v = next(g)
    if i == 2019:
        print(i, '###', v)  # part1
print(i, '###', next(g))
