import thirdPartyModule # written by Joe Shmoe

a = 0 
try:
    x = thirdPartyModule.bland(a)
except ZeroDivisionError:
    print('caught divide-by-0 attempt')
    x = 1000 #don't know x, proceed with 1000
except IOError:
    print('cannot open file')
    x = 1000 #don't know x, proceed with 1000
else:
    print("Inside 'else'...")
    y = 2*x
    print("Result is:", y)