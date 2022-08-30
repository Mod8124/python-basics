# Pythong - Basics

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