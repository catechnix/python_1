"""
*a function become a generator if it contains a yield
*generators return a generator object when called
*no code is executed when a generator is called
*iterating (or calling next() on the generator object executes all the code until the first yield
*once the yield is reached, the execution is paused and a value is returned.
*when another value is requested and the execution is resumed and the code executed until the next yield
*once the end of the function is reached, StopIteration is raised to signal that there are no more values

def gfibo(num):
  """Generate num fibonacci numbers"""
  fst, snd = 0, 1
  for x in range (num):
    yield fst
    fst,snd = snd, fst+snd
    
>>>gfibo(10)
generator object ... #no code is executed when calling generator
>>>list(_)
[0,1,1,2,3,5,8,13,21,34]
>>> for f in gfibo(10):
  print(f,end=' ')
  
0,1,1,2,3,5,8,13,21,34
  





"""
