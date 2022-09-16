# Pythong - Basics
I am just learning python by myself because i want to learn **django**..

# Table of Contents
- [Variable](#variables)
- [Comment](#comment)
- [Data-types](#data-types)
- [Casting](#casting)
- [Number](#number)
- [String](#string)
- [Boolean](#boolean)
- [Operator](#operators)
- [List](#list)
- [Tupple](#tupple)
- [Set](#set)
- [Dictionaries](#dictionaries)
- [If..else](#if-else)
- [Functions](#functions)
- [Class](#clases)
- [Inheritance](#inheritance)
- [Interator](#iterators)
- [Scope](#scope)

# variables 
`x = 5`

# comment

`# comments`

# Data Types

```python
 text : str()

 Numeric Types : int(), float(), complex()

 Sequence Types : list(), Tupple(), complex

 Mapping Types : dist

 Set Types : set(), frozenset()

 boolean Type : bool()

 binary Types : bytes(), bytearray(), memoryview()

 None Type: NoneType()

```

### Get the type 

print(type(2))

#### Examples

```
x = 1j (complex)

x = ['apple', 'nana'] list

x = ('apple', 'bana') tuple

x= range(6) range

x = { 'name':'denis', 'age':2} dict

x = {'apple', 'banana'} set

x = b"hello" bytes

x = bytearray(5) bytearray 

x = None

```
# Casting
"Specify" XD the type 

### casting is the same to covert 

x = int(10)
x = int('10')

# Number
numbers are the same that whatever language xD
- float
- int 
- complex(this is a number with letter)

# String
### multiline strings 
```python
   a = """eso ptedlk
   que tpaasdfasdw
   """ 
   # you can do with 

   a = '''esoo
    esoooo
   '''
```

#### methods
They're the same than js XD

#### format 
we have two ways insert manually or using format xd

```python
  age = 22;
  Im = 'I\'m {age} years old';

  print(Im)
  # I'm 22 years old

  age = 22;
  Im = 'I\'m {} years old';
  print(Im.format(age));
  # It's a unlimited xd

  # also you can put in order you want it
    quantity = 3
    itemno = 567
    price = 49.95
    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(quantity, itemno, price))
    # I want to pay 49.95 dollars for 3 pieces of item 567
```

# boolean

if it has some sort of content if going to return true except empty, 0 and None or whatever type empy for example `bool({}) = false`
```python
    bool('eso')
    # true
```

# Operators

all are teh same XD

execept that 
- `==` are equal
- `!=` not equal

logical operator
- `and` is the equal to '&&' 
- `or` is the equal to '||'
- `not` is equal to '!'

#### identity Operators
- `is` return boolean example x is 5
- `is not` the save but reverse XD

#### Membership Operator
- `in` loop inside a element a return true, if is inside 
- `not in` the same thing but reverse lol 

# list
It's a collection that is ordered and **muteable** (allow duplicated) also list is the same that array xD
`number = [1,2, 3, 4]`
`list((1,2,3))` create a list with casting

#### get the len
`len(number)` return the length of number 

#### change a range of item values 
```python
  numbs = [1, 2, 3,4]
  numbs[0,1] = [22, 10]
  #[22, 10, 3, 4]
```

#### insert 
insert a value in the list
```python
numbs = [1, 2,3]
numbs.insert(0, 'esoo')
#first position(index), secon parameter value
```

#### Append
insert add value in the last index
`append(value)`

#### extend 
is the same the concat on arrays also accept whatever data type of list, tupple, dictionary
`array1.extend(array2) = [...arrya1, ...array2]`

#### Remove 
Remove a specify element **omg**

```python
numbs = [1, 2,3,4]
numbs.remove(2)
```

#### pop 
remove the last index
`numbs.pop()`

#### del
keyword specified index
`del numbs[0]`

#### clear
clear the arrays **omg**

#### loops
loops in list
```python
for x in numbs:
  print(x)

```

also for runs with index, there is something called `range` range is like a list 
```python
for x in range(10)
# is going to print from zero to ten why ? idk

also you can do this
for x in range(len([1, 2,3]))
#x is going to be index of length []
#print the element [][x] xD
```

#### while
is the same thing xddd while condition is true repeat but there is something
interesting if it's false has else example
```python
 count = 0
 while 0 < 2:
  print(count)
  # 0 
  #1 
  #2
  else:
    print('finish)
  #finish
```

#### list Compresion
shortcout for interat list xddddd
`new = [variable for in iterable if condition`
```python
newlist = [x for x in fruits if "a" in x]
# instead
for x in fruits:
  if "a" in x:
    newlist.append(x)
```

#### Sort list
this method is **case sensitive**
thisList = []
thisList.sort()
- reverse
reverse all elements but has `reverse and sort(reverse=true)`
`thisList.sort(reverse=true)`

- desative case sensitive
`thisList.sort(key=str.lower)`

#### copy lists
reference = `list2 = list1` is just a reference so if list1 change list2 is goint to change too `list2 = list1.copy()` || `list2 =list(list1)` (unmuteable)

#### Count 
count how many times are in the list

#### index 
return the index of the element 
`list.index(1) = 0`

# tupple 
`thisTupple = (1, 2,3,4)`
- It's a **unchangeable**
- It's ordered
- It's indexed
- Allow duplicates
- Unpack available
- Can have any data type

### tupple Constructor
`tupple((1, 2, 3))`

#### tupple slice(range of indexes)
`thisTupple[2:5]`

### Hack the system
First tupple then covert to list change the value and then return again a tupple XD
for add or remove is to convert a list then again to tupple
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
```

### loop Tupple
It the same lfamo xD
`for x in tupple` || `for x in range(len(tupple))`


### join
this is interesting xd
```python
 tupple = (1, 2, 3,4)
 tupple2 = tupple * 2 
 # 1, 2, 3, 4, 1, 2, 3 ,4
```

# Set
`thisSet = {1, 2, 3}`
- Multiple values in single line
- unordered 
- unmuteable
- unindexed
- duplicates **not** allowed
- Any data is available XD

### Get the len
is the same xd

### Set Constructor
`set((1, 2, 3))`

### acces item 
`for x in thisset
  print(x)`

**you can add items** but **not change**

### Join to sets
`thiset.update(thiset2)`
`thisset.union(set2)`

`thiset.intersection(thisset2)` only contains (that repeats ones)
`thiset.difference(thiset2)` only contains(**not** reapeat ones)

### remove a item 
`thisset.remove('banana')`
if the item doesn't exits will raise an error

### discard a item 
`thisset.discard('banana)`
same but **not** will raise an error

### delete a element aleatory 
`thisset.pop()`

### clear the set
`thisset.clear()`

### Remove complete the set
`del thisset`

# Dictionaries
dictionaries are like objects xddddddddd
- store data in `key` and `values`
- not **allow duplicates**
- changeable
- ordered
- any data

`thisdict = {
  'name':'denis',
  'age':22
}`

- has len

### get the item 
`thisdict['name']` or `thisdict.get('name')`

### get the key
`thisdict.keys()`

##3 get the values
`thisdict.values()`

### get Items
`thisdict.items()` return the elemetn in list

### check if the key exits
`if 'hola' in thisdict:
    print('eso')

### add items 

`thisdict = {} thisdict['name'] = 'denis'`;`
`thisdict = {} thisdict.update({"instagram":"red"});`

### removing items
`thisdict = {} thisdict.pop('model');`

### removing item
`thisdict.popitem();`
`del thisdict['name'];`

### clear the dict
`thisdict.clear()`

### loop dictionaries
` for x in thisdict:
  print(x)
` return keys

`for x in thisdict:
  print(thisdict[x])
` return the values

`
  for x in thisdict.values():
  print(x)
`

`
  for x, y in thisdict.items():
  print(x, y)
` return key and values


### Copy Dictionaires
`x = thisdict.copy()` or `x = dict(thisdict)`

### methods
- clear()
- copy()
- fromKeys()
- get()
- items()
- keys()
- pop() 'especify keys'
- popitem() 'last inserted remove'
- update()
- values()

# If else
- equal `a == b`
- not equal `a !=B`

### if and else if
if the previous conditions were not true, then try this condition
```python
  if a == b:
    print('hola')
  elif c != C:
    print('no')
```
### the pass statement
```python
  if b > a:
    pass
```

# Functions

```python
def my_function():
  print('blog')
```

a **parameter** is the variable listed inside the parentheses
a **argument** is the value that sent to the function when it's called

### Manuy arguments but you dk how many
```python
def hola(*greeds):
  print(greegs)
```
### Functions emptys
```python
  def myFunction():
    pass
```

# Lambda
is like small function or arrow functions xd, the power of lamdba function is to use inside another function xd
`x = lambda a : a + 10` = `x lambda argument argumen2 : argument + argument2`
`print(x(10,10)`

# Clases
Something particulary about class in python if you print the class, it doesn't return the keys inside of the class 
`class MyClass:
  x = 5
`
this is bad practices xd
`
class Person:
  def __init__(self, name, age):
   self.name = name
    self.age = age
`
this is good practices the init run when class it's execute

### Function inside the class
The self inside the function refer to the class itself ** the self it doesn't have to call self** xd, if you create a function inside the class need to have a self **parameter**
```python
class Person:
  def __init__(self)

  def myFunc(self):
```

### delete object properties
`del person.name`

### delete object of the class
`del person`

# Inheritance
Inheritance allows us to define a class all the methods and properties from another class xd
```python
class Person:
  def __init__(self, name)
    self.name = name
class Student(Person):
   pass
# if you dont' have to pass

class Student(Person):
  def __init__(self, name , year)
   self.year = year
   Person.__init__(self, name)

```

### Super 
let you pass also the function of class
```python
 class Student(Person):
  def __init__(self, name, year)
    super().__init__(name)

    def sayHi(self):
      print(self.name + self.year)
```

# Iterators
i dk what are they useful but it's like a slider xddddddd by default `for x in something` has this behaviour but automally

```python
list = ('banana', 'fresa', 'melon')
interlist = iter(list)

print(next(interlist))
# banana
```

# Scope 
it's the same thing xddd that js

# Dates
A normal data xddd by the way python doesn't have date time(just import)

# Math
Math function xd
- `min` find the min numbers's range
- `max` find the max numbers's range
- `abs` return the number in positive way
- `pow` return the power of two numbers = a * a = a^a
- `import math`
 - `math.sqrt(n)` return the root of a number
 - `math.floor` return the lowest 
 - `math.ceil` return the highest
 - `math.pi` return the values of **api**

# Json
for handle **json** `import json`

json to python `json.loads(x)`
python to json `json.dumps(x)` by the way you can format

# pip 
it's for handling package on python

# try and catchs
```python
 try:
  print(x)
except:
  print('error')
```
### throw error
`raise TypeError('only interger')`

# Input
`input(text)`




