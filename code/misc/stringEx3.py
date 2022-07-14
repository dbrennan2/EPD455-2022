#!/usr/bin/env python3

aString = "This is" + " " + "a stRing"
bString = aString + 10*"!"
print("bString is:", bString)
print("Its length is:", len(bString))
print("aString is part of bString:", aString in bString)
