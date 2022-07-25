#! /bin/sh

#Matt Hamilton
#Module 05 Homework
clear


echo -e "Welcome to the Soda Emporium! We have EvEryThInG\n"
echo "BUT, you can only use the coins native to Soda Town."
echo -e "Nickels (5), Dimes (10), and Quarters (25).\n"

read -p "What type of soda would you like today?: " user_choice


soda_price=$((((($RANDOM%7)-3)*5)+100))
TOTAL=$soda_price
CHANGE=0
echo -e "The current price of $user_choice is $soda_price.\n"


while [[ $TOTAL -gt 1 ]];
do
	read -p "Please insert a coin: " coin_choice
	
	if [[ $coin_choice -gt $TOTAL ]];then
		CHANGE=$(($coin_choice - $TOTAL))
		echo -e "Your change of $CHANGE cents has been dispensed below.\n"
		break

	elif [[ $coin_choice == 5 ]];then
		echo "you have inserted a nickel."
		TOTAL=$(($TOTAL - $coin_choice))
		echo -e "you still owe $TOTAL\n"
	elif [[ $coin_choice == 10 ]];then
		echo "you have inserted a dime."
		TOTAL=$(($TOTAL - $coin_choice))
		echo -e "you still owe $TOTAL\n"
	elif [[ $coin_choice == 25 ]];then
		echo "you have inserted a quarter."
		TOTAL=$(($TOTAL - $coin_choice))
		echo -e "you still owe $TOTAL\n"
	else
		echo -e "woah woah woah, that was NOT a valid coin."
	fi
done

echo -e "Your $user_choice is being dispensed. Thank you!\n"

read -p "Press Enter to close the script."

