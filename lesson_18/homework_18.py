# homework 18

# ГЕНЕРАТОРИ
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# ІТЕРАТОРИ
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


class EvenRange:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


# ДЕКОРАТОРИ
def log_args_results(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result

    return wrapper


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Exception in {func.__name__}: {e}")
            return None

    return wrapper


# ПРИКЛАДИ


@log_args_results
def multiply(a, b):
    return a * b


@handle_exceptions
def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("\nEven numbers to 10:")
    for n in even_numbers(10):
        print(n, end=" ")

    print("\n\nFibonacci to 20:")
    for f in fibonacci(20):
        print(f, end=" ")

    print("\n\nReverse of [1, 2, 3, 4]:")
    for val in ReverseIterator([1, 2, 3, 4]):
        print(val, end=" ")

    print("\n\nEven range to 10:")
    for val in EvenRange(10):
        print(val, end=" ")

    print("\n\nMultiply and divide with decorators:")
    multiply(3, 5)
    divide(10, 2)
    divide(5, 0)
