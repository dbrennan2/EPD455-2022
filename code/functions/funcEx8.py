def foo(firstVal, secondVal):
    firstVal += 1
    secondVal -= 1  

def bar(firstVal, secondVal):
    firstVal += 2
    secondVal -= 2
    return firstVal, secondVal  

# -------------------
i = 1 
j = 39

foo(i,j) 
print("After foo function call:%2d and %2d" % (i, j))

bar(i,j) # good stuff returned, but not picked up
print("After first bar function call:%2d and %2d" % (i, j))

i, j = bar(i,j) # good stuff returned, and also picked up
print("After second bar function call:%2d and %2d" % (i, j))
