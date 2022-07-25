##Matthew Hamilton
##Mod 01 Homework

BASEPRICE = 100

RANDPRICE = 0

PAIDAMT = 0

print ('Welcome to the Soda Emporium! We have EvEryThInG')
soda_input = input('\nWhat type of soda would you like today? ')



import random

for i in range (-3,3):
    RANDPRICE = random.randint(-3,3) *5

TOTALPRICE = BASEPRICE + RANDPRICE

print ('\nOh ya homie, ', soda_input,' is only ', TOTALPRICE, 'cents.')

while True:
    COIN = input('Go ahead and insert a coin please: ')
    Converted_COIN = int(COIN)
    PAIDAMT = Converted_COIN + PAIDAMT
    BALANCE = TOTALPRICE - PAIDAMT
    if BALANCE > 0:
        print ('Insert', BALANCE, 'more cents please')
    elif BALANCE < 0:
        print ('You have', abs(BALANCE), 'cents as your change.')
        break
    else:
        break

print ('Enjoy your', soda_input, 'and have a wonderful day!')


print('\n\nPress Enter to end the script')
print('Press Enter to end the script')
input()

