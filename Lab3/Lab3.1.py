def binom(n):
    x = ""
    if n > 0:
        for step in range(n):
            x += "(a+b)"
        return x
    elif n == 0:
        x = "1"
        return x
    elif n < 0:
        for step in range(n * (-1)):
            x += "(a+b)"
        x = "1 / (" + x + ")"
        return x


nInput = int(input())
print(binom(nInput))
