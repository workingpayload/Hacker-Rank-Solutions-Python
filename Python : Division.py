if __name__ == '__main__':
    a = int(input())
    b = int(input())


def divide(a, b):
    c = a // b
    return c


def divide2(a, b):
    d = a / b
    return d


value = divide(a, b)
value2 = divide2(a, b)

print(int(value))
print(float(value2))

