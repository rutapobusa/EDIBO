Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> dir(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dir(a)
NameError: name 'a' is not defined
>>> type
<class 'type'>
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> 
