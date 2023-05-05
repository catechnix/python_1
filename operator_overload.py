###
__repr__:
  used by repr()
  used by str() if __str__ is not defined
  formal representation
  useful for debugging
__str__:
  used by str(), print(), and format()
  nice/informal representation
__init__
__bool_
__byte__

operator overloading:
  In python, it is possible to define how instances of a certain class interact with operators
    if instance compare equal or not -- ==, !=
    what is the result of the operations, like addition +
    if and how indexing/slicing is supported (inst[i])
   
Use the operator, acutally call the operator method:
  3+2
  (3).__add(2)__
  'xyz'*3
  'xyz'.__mul__(3)
  'xyz'[0]
  'xyz'.__getitem__[0]
  
  
  
  
  
  
  ###
