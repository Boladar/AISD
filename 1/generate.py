import random

def generate_tests(data_types,size):
    tests = []
    for t in data_types:
        tests.append(t(size))

    return tests

def up(size):
    table = []
    for i in range(0,size):
        table.append(i)

    return table

def down(size):
    table = []
    counter = size
    for i in range(0,size):
        table.append(counter)
        counter -= 1
    
    return table

def a(size):
    table = []
    counter = 1
    for i in range(1,size):
        table.append(counter)

        if i < size/2:
            counter += 1
        else:
            counter -= 1

    return table

def v(size):
    table = []
    counter = size
    for i in range(1,size):
        table.append(counter)

        if i < size/2:
            counter -= 1
        else:
            counter += 1

    return table

def stale(size):
    table = []
    for i in range(0,size):
        table.append(1)

    return table

def randomised(size):
    table = []
    for i in range(0,size):
        table.append(random.randint(0,100))

    return table