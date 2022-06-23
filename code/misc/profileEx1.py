import timeit

# ONE APPROACH
# setup code
import_math = "import math"

# code snippet
code = """
def sum(a,b,c):
	tmp1 = math.sqrt(a) + math.atan(b) + math.sin(c)
	tmp2 = math.sqrt(a+1.0) + math.atan(b+2.0) + math.sin(c+0.13)
	return tmp1/tmp2
"""
# execute code above 100000 times
howManyTimes = 100000
execution_time = timeit.repeat(stmt=code, setup=import_math, number=howManyTimes)
print("Total Execution time:", execution_time, "seconds (for", howManyTimes, "runs)")

# ANOTHER APPROACH
# Here you can even pass the value of the arguments
import math
import functools

def sum(a,b,c):
	tmp1 = math.sqrt(a) + math.atan(b) + math.sin(c)
	tmp2 = math.sqrt(a+1.0) + math.atan(b+2.0) + math.sin(c+0.13)
	return tmp1/tmp2

aval = 0.1
bval = 0.3
cval = 0.04
timeTaken = timeit.Timer(functools.partial(sum, aval, bval, cval)) 
print(timeTaken.timeit(howManyTimes))