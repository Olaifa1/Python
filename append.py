Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = li[1,2,3,4,5,6]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x = li[1,2,3,4,5,6]
NameError: name 'li' is not defined
>>> x = [1,2,3,4,5]
>>> x
[1, 2, 3, 4, 5]
>>> type(x)
<class 'list'>
>>> bag = [ 'good', 1.34, 'scv2002', 3456666.34]
>>> bag
['good', 1.34, 'scv2002', 3456666.34]
>>> type(bag)
<class 'list'>
>>> bag.append('egg', 3452.34,)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    bag.append('egg', 3452.34,)
TypeError: append() takes exactly one argument (2 given)
>>> bag.append('egg', 3452.34)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    bag.append('egg', 3452.34)
TypeError: append() takes exactly one argument (2 given)
>>> bag.append("strike")
>>> bag
['good', 1.34, 'scv2002', 3456666.34, 'strike']
>>> 
TypeError: append() takes exactly one argument (2 given)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
