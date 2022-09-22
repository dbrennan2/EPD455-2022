x = ['sure', 'maybe']
y = ['why']

# function definition
# x is a name, just a token
def mimi(x):
    x.append('not')

print("x is:", x)
print("y is:", y)
mimi(y)
print("x is:", x)
print("y is:", y)
