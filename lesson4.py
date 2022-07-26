#Example for creating functions
#Example -1

def my_function(fname):
  print(fname + " This is the first name")

my_function("Shadeeb")
my_function("Max")
my_function("Zachary")

#Example -2
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Shadeeb", "H.")

#Example-3
# This will generate an error
#def my_function(fname, lname):
#  print(fname + " " + lname)

#my_function("Shadeeb")

#Example-4
# Doing calculations
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Example-5
# These set of examples focuses on basic algebra operation using Functions in python
# and their syntax 

um1, num2 = 15, 50
ans = add(num1, num2)
# Example-6
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2
 
 
print(square_value(21))
print(square_value(-49))







print(f"The addition of {num1} and {num2} results {ans}.")
