import random

def generateNumbers(n):
    a = []
    while len(a) != n:
        num = random.randint(2, n*5)
        if num not in a:
            a.append(num)
    return a