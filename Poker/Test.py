import functools
import time


class Iterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.counter = 0
        self.sum = 0

    def __iter__(self):
        self.counter = 0
        self.sum = 0
        return self

    def __next__(self):
        if self.counter < len(self.sequence):
            self.sum += self.sequence[self.counter]
            self.counter += 1
            return self.sum
        else:
            raise StopIteration



def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func()
        end = time.perf_counter()
        timeUsed = end - start
        print(f"{func.__name__} needed {timeUsed} seconds to finish")
        return value
    return wrapper_timer()


@timer
def test123():
    return "Hallo"


if __name__ == "__main__":
    print(test123)
