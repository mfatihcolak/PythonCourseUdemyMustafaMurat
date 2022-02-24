def Fibonacci():
    a=1
    b=1
    yield a
    yield b

    while True:
        a,b = b,a+b
        yield b
for sayi in Fibonacci():
    if (sayi > 1000000):
        break
    print(sayi)