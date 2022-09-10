# General Employee class
class Employee:
    # Constructor
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
    # Method to give raise by percent
    def giveRaise(self,percent):
        self.salary = self.salary + (self.salary * percent)
    # Method to print the work the employee does
    def work(self):
        print(self.name,"does stuff")
    # Overload to return meaningful information when print is called on an Employee instance
    def __repr__(self):
        return f"<Employee: name={self.name}, salary={self.salary}>"

# Chef is a subclass of Employee
class Chef(Employee):
    def __init__(self,name):
        # Call the Employee class constructor
        Employee.__init__(self,name,salary=50000)
    def work(self):
        # More specific work
        print(self.name,"makes food")

# Server is a subclass of Employee
class Server(Employee):
    def __init__(self,name):
        # Call the Employee class constructor
        Employee.__init__(self,name,salary=40000)
    def work(self):
        # More specific work
        print(self.name,"interfaces with customer")

# Our pizza robot is a chef
class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):
        # The robot only makes pizzas
        print(self.name,"makes pizzas")



if __name__ == "__main__":
    beepBoop = PizzaRobot('beepBoop')
    print(beepBoop)
    beepBoop.work()
    beepBoop.giveRaise(0.1)
    print(beepBoop)

