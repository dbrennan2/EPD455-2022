def funcArgumentEx(formalArg):
    formalArg += 9  
    print('Inside the function:', formalArg)
    print('Inside the function, printing jVar:', jVar)


# here starts the execution
i = 1 
jVar = 5
print('Before function call:', i)
funcArgumentEx(i) 
print('After function call:', i)