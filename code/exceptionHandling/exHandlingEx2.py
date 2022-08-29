try:
    print(1/0)
except ZeroDivisionError:
    print('caught divide-by-0 attempt')

print("Made it here...")
