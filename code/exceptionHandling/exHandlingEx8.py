# file handling

# 1) fragile; can go wrong
file = open('output.txt', 'a')
file.write('hello world!')
file.close()

# 2) nice, more robust solution
file = open('output.txt', 'a')
try:
	file.write('\nhello world!!')
finally:
	file.close()

# using with statement; best solution
with open('output.txt', 'a') as file:
	file.write('\nhello world!!!')
