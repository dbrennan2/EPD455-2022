#!/usr/bin/env python3

aString = "This is a stRing"
bString = "\"" + aString + "\""
cString = aString[:4] + "\t" + aString[4:]
dString = aString[:4] + "\n" + aString[5:]

print(aString)
print(bString)
print(cString)
print(dString)