def myfun(n):
  return lambda a : a * n

double = myfun(2)
triple = myfun(3)

#print(double(5))
#print(triple(5))

def foo(myfun, num1,num2):
    print(myfun(num1, num2))

#foo(lambda x, y : x + y, 6, 7)
foo(lambda x,y: x*y, 6, 7)
