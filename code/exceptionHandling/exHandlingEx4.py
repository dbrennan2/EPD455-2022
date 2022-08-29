try:
    f = open("someFileThatDoesntExist.yyy", 'r')
except:
    print("Catching everything here. Is this wise?")

# this is better, at least the type of exception is
# printed out (hopefully somebody sees/minds this)
try:
    print('2'+2)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
