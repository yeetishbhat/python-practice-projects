def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


sum = add(2,3,4,5,6,7)
print(sum)