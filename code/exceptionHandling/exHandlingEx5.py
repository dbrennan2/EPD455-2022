import thirdPartyModule # written by Joe Shmoe

a = 0 
try:
    x = thirdPartyModule.getFunky(a)
except ZeroDivisionError:
    print('caught divide-by-0 attempt')
    x = 1000 #don't know x, proceed with 1000
except IOError:
    print('cannot open file')
    x = 1000 #don't know x, proceed with 1000
except:
    print('this error is too much for me...')
    print('not handling anything except:')
    print('\t - ZeroDivisionError')
    print('\t - IOError')
    raise

print("Made it here...")
y = 2*x
print("Result is:", y)