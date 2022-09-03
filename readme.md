# Pythong - Basics
This is repository, I am just learning python by myself because i want to learn **django**..
## variables 
`x = 5`

## comment

`# comments`

## Data Types

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
## Casting
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
well, list is the same that array xD
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

