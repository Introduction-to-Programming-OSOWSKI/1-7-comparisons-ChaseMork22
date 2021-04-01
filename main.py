def greaterThan(x, y):
    if int(x > y):
        return  True
    else:
        return False

def lessThan(x, y):
    if int(x < y):
        return True
    else:
        return False

def equalTo(x, y):
    if int(x == y):
        return True
    else:
        return False

def greaterOrEqual(x, y):
    if int(x >= y):
        return True
    else:
        return False

def lessOrEqual(x, y):
    if int(x <= y):
        return True
    else:
        return False

print(greaterThan(156, 155))

print(lessThan(133, 156))

print(equalTo(155, 15))

print(greaterOrEqual(155, 154))

print(lessOrEqual(155, 156))