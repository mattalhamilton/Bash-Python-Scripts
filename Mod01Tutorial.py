####Matthew Hamilton
####Tutorial 1


print('\nTask 1')
print('Hello World')
input()

print('\nTask 2')
user_guess = input('Please enter an integer: ')
print (user_guess)
input()

print('\nTask 3')
user_guess = int(user_guess)
converted_user_guess = int(user_guess)
print(user_guess * 3)
print(converted_user_guess * 3)
user_guess = str(user_guess)
print(user_guess * 3)
print('I entered ' + user_guess)
##print('I entered ' + converted_user_guess)
##this line produces an error

print('\nTask 4')
for i in range (1,21,1):
    if(i % 2) == 0:
        print('Even')
    else:
        print('Odd')

for i in range (1,21,1):
    if i == 7:
        print('Snowflake')
    elif (i % 2) == 0:
        print('Even')
    else:
        print('Odd')
       
print('\nTask 5')

for i in range (1,int(input('Enter a number greater than 13: '))+1,1):
    if (i) == 7:
        print('Lucky')
    if(i == 13):
        print('Unlucky')
    elif(i % 2) == 0:
        print('Even')
    else:
        print('Odd')
      
print('\nTask 6')
while True:
    user_name = input('please state your First and Last name: ')
    if user_name == 'Matt Hamilton':
        break
    
print('\nTask 7')
counter = 0
while counter < 10:
    print(counter)
    counter += 1

print('\nTask 8')
import random

for i in range (0,5):
    random_value = random.randint(-10,10)
    print (random_value, end=" ")

print('\nPress Enter to end the script')
print('Press Enter to end the script')
input()
