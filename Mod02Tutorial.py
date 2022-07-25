##Matthew Hamilton
##Mod 02 Tutorial


import random


def rando_insert(thing_being_inserted):
    position = random.randint(0,9)
    my_list.insert(position, thing_being_inserted)


counter = 0
my_list = []

while counter < 10:
    list_item = input('Please enter a word or a number: ')
    my_list.append(list_item)
    counter += 1



ints_only = []

print('\nTask 1 - Check the length of the list\n')

print('This list has 10 items. ' + str(len(my_list) == 10 ))

print('\nTask 2 - Print the list\n')

print(my_list)

print('\nTask 3 - Swapping first item with the last item in the list then print the list.\n')

first_thing = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = first_thing
print(my_list)

print('\nTask 4 - Print the first 3 items in the list and the last three in the list.\n')

print(my_list[0:3], my_list[-3:])

print('\nTask 5 - Loop through and print all the items in the list.\n')

for i in my_list:
    print(i)

print('\nTask 6 - Use an IF statement to check to see if the word "cat" is \nin the list and let the user know.')

if 'cat' in my_list:
    print('\nThere is a cat in my list')
else:
    print('There is no cat in my list')

print('\nTask 7 - Get the name of a Marvel character from the user and pass that \nto a function that randomly inserts the name into the list (import random).')

another_item = input('\nPlease insert the name of a Marvel character: ')
rando_insert(another_item)

print('\nTask 8 - Get the index for the Marvel character and print it out so \nthat it looks nice.')

print(another_item + ' is at index ' + str(my_list.index(another_item)))

print('\nTask 9 - Copy all the integers in the original list to a new list, then sort and print out that list.')

for matt in my_list:
    try:
        int(matt)
        ints_only.append(int(matt))
    except:
        continue
ints_only.sort()
print ('\nThese are the integers from the list')
print (ints_only)

print('\nTask 10 - Convert the original list to a tuple and print the tuple.\n')

my_tuple = tuple(my_list)
print(my_tuple)

print('\nTask 11 - Try and change the first item in the tuple to "cat", but catch the error and print out Tuples are immutable!\n')

try:
    my_tuple[0] = 'cat'
except:
    print('Tuples are immutable!')

print('\nTask 12 - Copt this new list in the text box into your script.\n')

list_in_list = [[1,2,3],['a','b','c']]
for i in list_in_list:
    for j in i:
        print(j)

print()
print('press enter to end the script')
input()
