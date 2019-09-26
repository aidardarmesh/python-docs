x = lambda a: a + 10

print(x(5))

def multiplyer(n):
    return lambda x: x * n

doubler = multiplyer(2)
tripler = multiplyer(3)

print(doubler(11))
print(tripler(11))