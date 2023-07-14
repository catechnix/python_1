"""
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …

Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …

# Python program to illustrate functions
# Functions can return another function
  
def create_adder(x):
    def adder(y):
        return x+y
  
    return adder
  
add_15 = create_adder(15)
  
print (add_15(10))

"""
