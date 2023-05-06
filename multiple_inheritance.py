"""
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

Make sure all the base classes have super(), if it doesn't, it will stop there since there is no super(), won't call the next class

A mixin is a class that provides a certain functionality
Other classes can inherit from it to implement this functionality
Mixins are not supposed to be used on their own

How to use **kwargs:
class Named:
  """A mixin that sets the 'name' attribute """
  def __init__(self, *args, **kwargs):
    self.name = kwargs.pop('name')
    super().__init__(*args,**kwargs)
    
class Platypus(Beaver, Duck, Named):
  def sting(self):
    print("Stinging enemy...')
    
p = Platypus(name='Billy')
>>>p.name
>>>Billy






"""
