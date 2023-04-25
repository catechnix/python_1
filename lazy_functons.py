"""
Lazy functions-- 
*immediately return an iterable object
*elements are created one by one when requested, during iteration
*elements are discarded afterwards
*only one element in memory at a time
*more efficient
*allow handling of infinite sequences
map(), filter(),zip(),range(), enumerate()

map(function, iterables), input- a function and one or more iterables, output- a new lazy iterator that applies function to all the items and yields 
the results
similar to function (x) for x in iterable.
map() returns a lazy object, use list to see all the iterables -- list(map(abs,nums)

filter(function, iterable), input: a function and iterable, output: a new lazy iterator that yields the items for which function(item) is true, similar 
to [x for x in iterable if function(x)] but lazy

zip(*iterables): input- one or more iterables, output- a new lazy iterator that yields tuples, with the n-th tuple containing the n-th item of each iterable
zip(range, 'abc')
list(zip(range(3),'abc'))=>[(0,'x'),(1,'y'),(2,'c')] 

range()

enumerate(seq,start=0)

An iterable is an object capable of returning its members one at a time. Everything that you can use in a for loop is iterable, e.g. list, strings, files, dictionary
__getitem__ or __iter__ ->return an iterator

Iterators are objects that keep track of the position during iteration.

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

The yield expression: 
def func_name(args):
  yield result
  
Yield is used to pause the function and return a value
It is possible to resume the function
yield can be executed multiple times 
a function can have multiple yields
it is possible to yield multiple values
