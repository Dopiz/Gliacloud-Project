import re
import collections


def anonymous(x):
    return x ** 2 + 1

def integrate(func, start, end):
    step = 0.1
    intercept = start
    area = 0

    while intercept < end:
        intercept += step
        # Area = width * height
        area += step * func(intercept)
    
    return area


print(integrate(anonymous, 0, 10))