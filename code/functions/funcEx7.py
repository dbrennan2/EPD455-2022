#!/usr/bin/env python3

mimi = "global "
def foo():
    global mimi
    mimi = mimi * 2
    
foo()
print(mimi)
