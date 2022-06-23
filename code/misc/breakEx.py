#######################################
## Example: how "break" statement works
#######################################

accumulator = 0

for i in range(3, 14, 3):
    accumulator += i
    if accumulator >= 10:
        print('About to break out of this loop...')
        break
        # accumulator += 1
    
print(accumulator)