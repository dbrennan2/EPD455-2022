outf = open("data/writeout.txt", "w")
outf.write("Great to be around.\n")
outf.write("Smiling.\n")

# look at writing out data
x = [3.14159265359, 1.23456789]
outf.write(str(x) + "\n")
# use format, if you have special requests
outf.write('{:8.3e}\n'.format(x[0])) 
outf.close()