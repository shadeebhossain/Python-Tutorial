#Example-1
#Creating a class
class speed:
  distance = int(input("Please enter a distance:"))
  time=int(input("Please enter your time:"))
  s=distance/time
class acceleration:
    initial_velocity=int(input("Please enter initial velocity:"))
    final_velocity=int(input("Please enter final velocity:"))
    time=int(input("Please enter time:"))
    accel=(final_velocity-initial_velocity)/time
# Creating an object  
p1 = speed()
p2= acceleration()
print("The speed for Question 1 is:")
print(p1.s)
print("The acceleration for Question 2: ")
print(p2.accel)

#Example-2
#Using the built in function _init_()
class Speed_1:
  def __init__(self, distance, time):
    self.distance = distance
    self.time = time
    self.speed=distance/time
p1 = Speed_1(100, 30)

print("The speed for question 3 is:")
print(p1.speed)
#Example-3
# Inheritance
# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
 
 
class Person(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is an employee
    def isEmployee(self):
        return False
 
 
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
 
    # Here we return true
    def isEmployee(self):
        return True
 
 
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
 
emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
