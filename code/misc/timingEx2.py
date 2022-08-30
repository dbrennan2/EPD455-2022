# ANOTHER APPROACH FOR TIMING A FUNCTION
# Here you can even pass the value of the arguments
import timeit
import math
import functools


def sum(a, b, c):
    tmp = math.sqrt(a) + math.atan(b) + math.sin(c)
    return tmp**2


aval = 0.1
bval = 0.3
cval = 0.04
# callable created using functools and passed to the timer
timeTaken = timeit.Timer(functools.partial(sum, aval, bval, cval))
howManyTimes = 100000
print(timeTaken.timeit(howManyTimes))
