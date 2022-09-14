#!/usr/bin/env python3

def scopeExample():
    str = "You are nice."
    print(str)


# Global scope
str = "You are awesome."
scopeExample()
print(str)
