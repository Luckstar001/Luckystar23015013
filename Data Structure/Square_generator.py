
def squares():
    for i in range(1, 11):
        yield i ** 2
for square in squares():
    print(square)
