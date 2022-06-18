
someString = input("Type a float number, it'll be picked up as a string though: ")
print(someString) # prints here as a string
print("For doing math, need to convert string to float")
floatTypedIn = float(someString)
print("Doing math is ok upon conversion:")
print(3.3 + floatTypedIn)
print("Adding a float to a string not ok, leads to an error that stops Python:")
print(3.3 + someString)