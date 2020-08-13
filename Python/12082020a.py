Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> letter = fruit[0]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    letter = fruit[0]
NameError: name 'fruit' is not defined
>>> letter = fruit[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    letter = fruit[0]
NameError: name 'fruit' is not defined
>>> print(letter)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(letter)
NameError: name 'letter' is not defined
>>> fruit = 'banana'
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    letter = fruit[1.5]
TypeError: string indices must be integers
>>> len[fruit]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    len[fruit]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(fruit)
6
>>> fruit[1]+fruit[2]+fruit[3]+fruit[4]
'anan'
>>> fruit[0]+fruit[1]+fruit[2]+fruit[3]+fruit[4]+fruit[5]
'banana'
>>> fruit[N-1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    fruit[N-1]
NameError: name 'N' is not defined
>>> N=fruit-1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    N=fruit-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> N=[fruit-1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    N=[fruit-1]
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> N=(fruit-1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    N=(fruit-1)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> last = fruit[length-1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    last = fruit[length-1]
NameError: name 'length' is not defined
>>> print(last)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(last)
NameError: name 'last' is not defined
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
b
a
n
a
n
a
>>> index = 0
>>> while index >= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index +1

	
>>> while index >= len(fruit):
	letter = fruit[index]
	print(letter)
	index = index -1

	
>>> index=5
>>> while index >= 0:
	letter = fruit[index]
	print(letter)
	index = index -1

	
a
n
a
n
a
b
>>> 
