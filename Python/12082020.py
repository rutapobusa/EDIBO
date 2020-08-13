Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> a=10
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> a=10
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a=10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a=10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> a="adbs"
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
slikti
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tekstu neviens nekad neredzēs")
else:
	print("slikti")

	
slikti
>>> 
