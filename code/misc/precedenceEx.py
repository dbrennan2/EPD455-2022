#!/usr/bin/env python3
"""
precedenceEx.py: Makes the point that it's good to understand precedence.
"""

if True or False and False:
    print('True')
else:
    print('False')


if (True or False) and False:
    print('True')
else:
    print('False')
