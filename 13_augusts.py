# coding: utf-8
def f(): pass
f()
type(f)
def f(): print
def f(): print("Hello")
f()
type(f)
def g():
    a = 22
    print(a+3)
    
g()
def g(a):
    print(a+3)
    
g(a)
g(22)
g(123)
def g(a):
    c = a+3
    print(c)
    
g(123)
def h():
    c = a+b
    print(c)
    
def h():
    a=11
    b=33
    c = a+b
    print(c)
    
h()
def h():
    a=11; b=33
    c = a+b
    print(c)
    
h()
def h(a, b):
    c = a+b
    print(c)
    
h(46, 24)
def h(a, b):
    c = a*b
    print(c)
    
h(42,7)
def h(a, b):
    c = a/b
    print(c)
    
h(42,7)
def h(a, b):
    c = a+b*a-b
    print(c)
    
h(40, 5)
def h2(a=22, b=33):
    c = a+b*a-b
    print(c)
    
h2()
def h2(a=22, b=33):
    c = (a+b)*(a-b)
    print(c)
    
h2()
def h2(a=22, b=33):
    c = a+b
    print(c)
    
h2()
h2(3,4)
def f2(a, b):
    return (a+b)
    
f2(3,4)
print(f2(3,4))
get_ipython().run_line_magic('save', '13_augusts 1-39')
