'Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> list1 = [2,4,6,8,10,12]
>>> print(list1)
[2, 4, 6, 8, 10, 12]
>>> list2 = [2,4,6,8,10,12]
>>> list2 = [100,23.5,'hello']
>>> print(list2)
[100, 23.5, 'hello']
>>> list3  = [['physics', 101],['chemistry',202],['mathematics'303]]
  File "<stdin>", line 1
    list3  = [['physics', 101],['chemistry',202],['mathematics'303]]
                                                               ^
SyntaxError: invalid syntax
>>> list3 = [['physics', 101],['chemistry',202],['mathematics'303]]
  File "<stdin>", line 1
    list3 = [['physics', 101],['chemistry',202],['mathematics'303]]
                                                              ^
SyntaxError: invalid syntax
>>> list3  = [['physics',101],['chemestry',202],['methematics',303]]
>>> print(list3)
[['physics', 101], ['chemestry', 202], ['methematics', 303]]
>>> list[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> list1[0]
2
>>> list2[0]
100
>>> list1[50]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> list1[15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> list1[1+4]
12
>>> n = len(list1)
>>> print(n)
6
>>> list4 = ['red','green','blue','orange']
>>> print(list4)
['red', 'green', 'blue', 'orange']
>>> list4[3] = 'black'
>>> print(list4)
['red', 'green', 'blue', 'black']
>>> list4[2] = 'white'
>>> print(list4)
>>> print(list
['red', 'green', 'white', 'black']
>>> city = ('rajkot','surat','vadodara','mundra','goa')
>>> print(city)
('rajkot', 'surat', 'vadodara', 'mundra', 'goa')
>>> number = (1,2,3,4,5)
>>> print(number)
(1, 2, 3, 4, 5)
>>> mix_tuple = ('delhi',)
>>> mix_tuple = ('delhi','banglor','pune',1,2,3)
>>> print(mix_tuple)
('delhi', 'banglor', 'pune', 1, 2, 3)
>>> print(city[2])
vadodara
>>> print(city[-4])
surat
>>> print(city[-3])
vadodara
>>> print(city[1:4])
('surat', 'vadodara', 'mundra')
>>> city[2] = 'bombay'
Traceback (most recent call last):
TypeError: 'tuple' object does not support item assignment
>>> t3 = city+number
>>> print(t3)
('rajkot', 'surat', 'vadodara', 'mundra', 'goa', 1, 2, 3, 4, 5)
>>> del  = (city)
  File "<stdin>", line 1
    del  = (city)
         ^
    del  = (city)
SyntaxError: invalid syntax
>>> del(city)
>>> print(city)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'city' is not defined
>>> print(city)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'city' is not defined
>>> this_tupkle = ("apple","banana","chery","apple","chery")
>>> print(this_tuple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'this_tuple' is not defined
>>> print(this_tupkle)
('apple', 'banana', 'chery', 'apple', 'chery')
>>> this_tuple1 = ["apple","apple"]
>>> print(this_tuple1)
['apple', 'apple']
>>> print = (type(this_tupkle))
>>> print = type(list1)
>>> print = type(this_tuple1)
>>> print type(this_tuple1)
  File "<stdin>", line 1
    print type(this_tuple1)
          ^
SyntaxError: invalid syntax
>>> print type(this_tuple1)
  File "<stdin>", line 1
    print type(this_tuple1)
          ^
SyntaxError: invalid syntax
>>> print(this_tupkle[-1])
['c', 'h', 'e', 'r', 'y']
>>> print(this_tupkle[2:5])
['chery', 'apple', 'chery']
>>> print(this_tupkle[:4])
['apple', 'banana', 'chery', 'apple']
>>> print(this_tupkle[2:])
['chery', 'apple', 'chery']
>>>'