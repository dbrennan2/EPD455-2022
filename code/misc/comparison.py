a = 1
b = 1.0
c = '-1'

if a == b:
    print("int-to-float conversion takes place, and values are identical...")

if a > int(c):
    print('int-to-string comparison requires explicit conversion; works well.')

if a > c:
    print("Can't compare string to int...")
