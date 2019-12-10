s = 'Hello World concatenate me!'
#   To convert values of variable s to uppercase
s.upper()
print(s.upper())

s1 = 'Hello World concatenate me!'

#   To split values of variable s1.
s1.split('.')
print(s1.split())

s3 = 'Hello.World.concatenate.me!'

s3.split(',')
print(s3.split())

#   STRING FORMATTING
print('My name is %s and I am at %s' %('Waliu Olaifa','Semicolon village'))

print('My name is %s and I live at %d' %('Waliu Olaifa',312))

print('My name is %s and I live at %d' %('Waliu Olaifa',31.322))

print('My name is %s and I live at %i' %('Waliu Olaifa',312))


print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')

#       ALIGNMENT   
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))


num = 267453
print(f"My 10 character, four decimal number is:{num:10.4f}")

#   LISTS
#   A list can hold objects of diferent datatypes.
my_list = ['A string',23,100.232,'o']
len(my_list)

#   Indexing and Slicing
#   Grab index 1 amf everything pastit
my_list[1:]

li1 =[1,2,3]
li2 = [4,5,6]
li3 = [li1 + li2]

li3
id(li1)
id(li2)
id(li3)

li2 * 0

#   Use the keyword APPEND to add an item permanently at the end of a list
# list1.append('append me!')
li1.append('100,234')

#   Use pop to “pop off” an item from the list. By default pop takes off the last index, but you can
#   also specify which index to pop off. Let’s see an example:
li1.pop(1)

#   Assign the popped element, remember default popped index is -1
list1 = [2,3,4,5,6,7]
popped_item = list1.pop()

#   We can use the sort method and the reverse methods to also effect your lists:
new_list = ['a','e','x','b','c']
# Use reverse to reverse order (this is permanent!)
new_list.reverse()

#   Use sort to sort the list (in this case alphabetical order, but for numbers it will new_list.sort()
new_list.sort()

#   DICTIONARY
mxd = {1/3:1}

for k, m in enumerate(mxd):
    print(k,m)

    

