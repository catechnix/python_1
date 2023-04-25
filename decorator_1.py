import time
import random

def calc_time(func):
  def inner (*args, **kwargs):
    start = time.time()
    res = func(*args, **kwargs)
    end = time.time()
    print ('The function took', end - start, 'seconds.')
    return res
  return inner

@calc_time
def stupid_sort(input_seq):
  """shuffle until sorted"""
  seq = list(input_seq)
  while seq != sorted(seq):
    random.shuffle(seq)
    return seq
  
@calc_time
def smart_sort(seq):
  """Sort and return"""
  return sorted(seq)

"""range(10,0,-1): starts from 10, decrease by 1 and ends with 1"""

"""
iterable: object that can be iterated
iterator: object that keeps track of the iteration
create a iterable: iterable = 'An Iternable Object'
create two iterators: 
iterator1 = iter(iterable) 
iterator2 = iter(iterable)   
next(iterator, default)
z=zip('xyz', '246')
next(z)->('x','2')
next(z)->('y','4')
