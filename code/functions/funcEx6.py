#!/usr/bin/env python3

def foo(iVal):
    iVal += 9  
    print('Inside the function:', iVal)


# -------------------
i = 1 
foo(i) 
print('After function call:', i)