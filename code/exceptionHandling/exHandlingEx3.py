import thirdPartyModule # written by Joe Shmoe

a = 0 
try:
    x = thirdPartyModule.thirdPartyFunction(a)
except ZeroDivisionError:
    print('caught divide-by-0 attempt')
    x = 1000

print("Made it here...")
y = 2*x
print("Result is:", y)