# @author : HUSSAIN ASHIQ
# @Description: This code shows some comcepts of OOP in python


# class 1 : Student Class
class Student:
    name = "" #class attribute
    college = "MCS" #default value
    semester = ""
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester
    def introduce(self):
        print("My name is {} and I a stduent of {}, studying {} semester.".format(self.name, self.college, self.semester))

student1 = Student("HUSSAIN ASHIQ", "5TH")
student1.introduce()

## ======================================================================================
# class 2: Software Engineering Student inherting from Student class
# demontrating inhertance : SE student is a Student

class SE_Student(Student):
    department = "CSE"
    def __init__(self, name, semester):
        super().__init__(name, semester)
    def whoami(self):
        print(f"I am {self.name} and I am an CSE student.")

se_std = SE_Student("KHATTAK", "5TH")
se_std.introduce()
se_std.whoami()
## ======================================================================================
# class 3: Electrical Engineering Student inherting from Student class
# demontrating inhertance : SE student is a Student
class EE_Student(Student):
    department = "EE"
    def __init__(self, name, semester):
        super().__init__(name, semester)
    def whoami(self):
        print(f"I am {self.name} and I am an EE student.")

ee_std = EE_Student("HAMZA", "5TH")
ee_std.introduce()
ee_std.whoami()
## ======================================================================================
# class 4 : Computer class
# demo of Encapsuation
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
# change the price
c.__maxprice = 1000 #no effect since the __maxprice is a private attribute.
c.sell()
# using setter function
c.setMaxPrice(1000)
c.sell()

## ======================================================================================
# Class 5 - Polymorphism
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
# However we could use the same method to color any shape. This concept is called Polymorphism.

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

## ======================================================================================