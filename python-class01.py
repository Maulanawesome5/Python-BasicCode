class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.garduationyear = year
        #Person.__init__(self, fname, lname)
    #pass
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.garduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
# print(x.garduationyear)
# x = Person("John", "Doe")
# x.printname()