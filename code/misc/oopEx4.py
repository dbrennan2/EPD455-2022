class human:
    """"A class representing a human"""
    def __init__(self, n):
        self.name = n

    def get_age(self):
        return self.age

    def set_age(self, a):
        self.age = a

    def human_info(self):
        print('Name: ', self.name)
        print('Age: ', self.age)

mary = human('Mary')
mary.set_age(39.5)
mary.human_info()