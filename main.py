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

def lessorEqual(x, y):
    if int(x <= y):
        return True
    else:
        return False

print(greaterOrEqual(156, 155))
