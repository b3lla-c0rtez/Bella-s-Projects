Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3 + 4
7
>>> 10 / 2
5.0
>>> 3 * 5
15
>>> 2 ** 3
8
>>> 14 / 3
4.666666666666667
>>> 14 // 3
4
>>> 14 % 3
2
>>> type(3)
<class 'int'>
>>> type(3.0)
<class 'float'>
>>> type("3.0")
<class 'str'>
>>> type('3.0')
<class 'str'>
>>> 10 /0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> cost = 50
>>> type(cost)
<class 'int'>
>>> discount = 0.10
>>> type(discount)
<class 'float'>
>>> discounted_cost = cost - cost * discount
>>> discounted_cost
45.0
>>> print(discounted_cost)
45.0
>>> print("Discounted cost:", discounted_cost)
Discounted cost: 45.0
>>> 'Cortez' + 'Isabella'
'CortezIsabella'
>>> 'Cortez' + ' ' + 'Isabella'
'Cortez Isabella'
>>> 3 * 'A'
'AAA'
>>> 3 * 4 * 'A'
'AAAAAAAAAAAA'
>>> 2 * '4'
'44'
>>> 2 * 4
8
>>> 2.0 * 'AA'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> 0.50 * 'AA'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> 'Discount: ' + 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'Discount: ' + 45