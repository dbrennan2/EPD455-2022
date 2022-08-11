class human:
    """"A class representing a human"""
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def __str__(self) :
        dummy = self.name
        dummy += ", age "
        dummy += '%s' % self.age
        dummy +=  "."  
        return dummy

    def __add__ (self,nyears):
        self.age += nyears

    def __lt__(self,dummy):
        return self.age < dummy.age

bibi = human('Bibi',55)
mary = human('Mary',39)
mimi = human('Mimi',64)
print(mary.name + " is younger than " + bibi.name + ": ")
print(str(mary<bibi))
humans = [mimi, mary, bibi]
for s in humans: print(s)
humans.sort()
print("sorted now:")
for s in humans: print(s)
