numbs = [1, 2, 3, 4]
if 1 in numbs:
    print('if one is in numbs');
else :
    print('esooo')

def eso():
    if 1 in numbs:
        return 'if one is in there'
    else:
        return 'if not there'
print(eso())

numbs[0:1] = [22, 10]
print(numbs)

# insert
numbs.insert(3, 'esooo')
# first parament
print(numbs)

numbs.append(100)
print(numbs)

# loops in list
for x in ['eso1','eso2']:
    print(x)

for x in range(10):
    print(x)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print('line......')
thislist.sort()
print(thislist)

# reverse
eso = thislist.sort(reverse=True)
print(eso);

# count 
#count how many time are in the list
