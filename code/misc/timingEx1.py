import timeit

# setup
impMath = "import math"

# code snippet
code = """
def sum(a,b,c):
	tmp1 = math.sqrt(a) + math.atan(b) + math.sin(c)
	return tmp1**2
"""

# execute code above 100000 times
howManyTimes = 100000
execution_time = timeit.repeat(stmt=code, setup=impMath, repeat = 5, number=howManyTimes)
print("Execution time:", execution_time, "seconds (for", howManyTimes, "runs)")
