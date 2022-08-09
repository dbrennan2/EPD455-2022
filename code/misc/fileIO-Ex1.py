myFile = open("data/readin.txt", "r")
myString = myFile.read()
print("Content of the file:\n", myString)

yourFile = open("data/readin.txt", "r")
stringList = yourFile.readlines()
print("A list, one line per list element:\n", stringList)

