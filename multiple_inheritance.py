###
class Base1:
  pass

class Base2:
  pass

class SubClass(Base1, Base2):
  pass

Subclasses inherit all the methods of all the base classes

MRO: method resolution order (MRO)
* Classes have a special __mro__ attribute
* __mro__ is a tuple of classes
* while acccessing an attribute, these classes are visited one after the other
* The order is determined by using the C3 linearization algorithm








###
