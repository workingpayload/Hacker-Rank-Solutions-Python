if __name__ == '__main__':
    a = int(input())
    b = int(input())


def sum(a, b):
    c = a + b
    return c


def sub(a, b):
    d = a - b
    return d


def multiply(a, b):
    e = a * b
    return e


add = sum(a, b)
minus = sub(a, b)
multi = multiply(a, b)

print(add)
print(minus)
print(multi)
