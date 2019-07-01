from math import factorial


def get_nth_triangle(num):
    total = 0
    while num > 0:
        total += num
        num -= 1
    return total


for i in range(20):
    print "Base {} nth Triangle: {} Factorial: {}".format(i, get_nth_triangle(i), factorial(i))