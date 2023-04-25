"""
The contextlib module defines a @contextmanager decorator that can
create new context managers by using yield:
>>>@contextmanager
  def mycm():
    print("start')
    yield
    print('end')
    
>>>with mycm()
  print(test)
 ....
 ....
 start
 test
 end
 
 The body of mycm() is executed till yield where it is paused, then the body of the with is executed.







"""
