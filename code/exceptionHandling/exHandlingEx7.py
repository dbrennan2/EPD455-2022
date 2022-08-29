class MyException(Exception):
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return self.value


try: 
    # just raise right away, to make a point...
    raise MyException(2*2) 
except MyException as e:
    print("My exception occurred, value: ", e.value)

print("Crashing now - exception thrown not handled:")
raise MyException('oops!')

