# created variables and assing
# normal
a = '10';
b = '10';


# Casting
c = int(a);
# c is equal to 10


# multiples variables 

x, y, z = 'orange', 'eso', 'siiuuu',
print(x, y, z)
# it's like a destructuring in js

# unpack Collection 

numbers = [1, 2, 3]
x, y, z = numbers
# print(x, y, z) = 1, 2, 3

# python has global and local variables 

x = 1

def hola():
    x = 2;
   # global x keyboard reserved for to local to global variables
    print(x);
hola()


