# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples share a few similarities, but there difference lies in that lists are mutable and tuples are immutable. Both are iterable and store data in array-like ways. Tuples work as keys in dictionaries, as far as I can tell, in simplest terms, because they are hashable where as lists are not. Immutability is a nice feature for a key, so that we cannot alter the order or input anything further into a key value once it has been created.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

lists are mutable and are unordered. They can contain any number of repeating alues. Sets, on the other hand, can only contain unique values and such values must be hashable, whereas lists do not care about that. 

a list:
```python
simple_list = [1,2,2,3,3,4,4,5,5,5]
```
finding a set of the same list:
```python
simple_set = {1,2,3,4,5}
```
Lists are more flexible and can store multiple copies of a value, Sets on the other hand are hashable and a faster option for recalling values. Lists have a time complexity of O(n) for recal of a value and sets have a time complexity of O(1).
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.
A lambda function is what is known as an anonymous function and are functions made of a single expression. They are defined using the lambda keyword. (lambda x: x+2) will return any integer value will be incremented by 2. 

A short example, sorting by how divisible something is by a value, either making it odd or even.
```python
>>> sorted([100,2,12,6,90],key = lambda x: x%3 == 0)
[100, 2, 12, 6, 90]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is a syntatic way to make a list based on an existing list. It works similarly to amathematical function in syntax. It is simply more concise and readable.
The following produces a list, using list comprehension of every value from 0 to 9 squared.
```python
>>[x**2 for x in range(0,10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

For `map`:
```python
>>>map(lambda x:x**2, range(0,10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
for `filter':
```python
>>>filter(lambda x: x%2 == 0,range(0,10))
[0, 2, 4, 6, 8]
>>>[x for x in range(0,10) if x%2 ==0]
[0, 2, 4, 6, 8]
```
they both have the same output.

For set comprehension:
```python
>>> {random.randint(0,10) for x in range(10)}
set([1, 3, 4, 7, 9, 10])

```
As a general example for dict comprehension we have:
```python
d = {key: value for (key, value) in iterable}
```

```python
>>> {n: (n**2)%2 for n in range(0,10)}
{0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 1}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

```python 
>>>change = datetime.datetime(2015,07,28)-datetime.datetime(2013,01,01)
>>>change.days
938
```
That is, 938 days will have passed.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
For this time difference the change in days would be 513.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```


There is a 7840 day difference between the start and stop dates.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





