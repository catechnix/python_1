"""
*a generator expression (genexp) is an expression that creates a generator object
*Its syntax is similar to a list comprehension, but the expression is enclosed within ():
(expr for elem in seq)

g=(x for x in range(10) if x%2 ==0)
g
generator object <genexpr> at 0xbdkskks>
list(g)
[0,2,4,6,8]

Functions have 1 entry point and 1 exit point
Generators have 1 entry point and multiple exit points
Coroutines have multiple entry points and multiple exit points

coroutines are implemented with generators. In addition to support iteration, generators also 3 methods:
*g.send(value)
*g.throw(exception)
*g.close()





"""
