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

Attributes:
* attributes are variables defined within a class:
class ClassName:
  clsattr=value
  def method(self):
    self.insattr=value
There are two types of attributes: class.attribute and instance.attribute

Two ways to define and access the attribute:
* define inside the class 
* ClassName.attrubute = value
* Inst.attr = value, if not inst attr, python will look class attr

__init__ method: is a special method, it is used to create an instance, is called whenever a new instance is created.

>>>class InitTest:
      def __init__(self):
          print('__init__ called')
>>>inst1 = InitTest()
__init__ called!

It is possible to pass arguments to __init__ during class instantiation:
>>>class Dog:
      def __init__(self, name):
          self.name= name #define instance att
      def bark(self):
          print(self.name, 'says bark')
>>> rex = Dog('Rex')
>>> rex.name
>>> 'Rex'

__init__ is used to initialize instance
when an instance is created with Class(args), the args are passed to the __init__ method
Instance attributes are usually defined in the __init__method
__init__ is not a constructor (the instance has already been created and passed to __init__ as first argument(self)





"""
