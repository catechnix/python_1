"""
python supports several paradigms:
imperative/procedural
functional
object-oriented

object-oriented programming is a programming paradigm:
* based on concept of object
* an object is a bundle of states and behaviour
* the state is stored in variables known as attributes
* the behaviour is defined by functions defined within the class, known as methods
* the type of object is defined by a class
* the class is used to create several instances

A class is an abstract model of an objedt, define the struture of the object. An instance(object) is a concrete object, has struture defined by the class.
A single class is used to create multiple objects.

attributes and methods are tied to an object: obj.attribute: to access an attribute, obj.method: to call a method

Inheritance:
*classes can be used to define subclasses
*subclasses inherit all the methods and attributes of the base class(super class)
*subclasses can extend/modify the base class
*a subclass can inherit from more base classes

class ClassName:
  attribute = value
  def method(self):
    pass
   
*class is used to define new classes
*class name is used CamelCase
*followed by indented block with attributes and methods of the class, in the body of the class, define attribute and methods

class are objects too like everything else in python, ClassName is a variable that refers to the class object
class are callable -- inst1=ClassName(), inst2=ClassName()



"""
