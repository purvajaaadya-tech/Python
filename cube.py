def cube(num):
    return num * num * num

def b3(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False

print(b3(9))
print(b3(4))