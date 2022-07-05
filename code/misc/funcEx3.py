
def funcArgumentEx(formalArg):
    formalArg += 9  # now the name formalArg points to object "10"
    print('Inside the function:', formalArg)


# here starts the main function
i = 1 
print('Before function call:', i)
funcArgumentEx(i) # i is the actual argument passed to function
print('After function call:', i)