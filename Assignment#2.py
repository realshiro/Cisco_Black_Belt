import random

Random_number = random.randint(0, 10)
Guess_number = input("Guess the number: ")

if(Guess_number==Random_number):
	print("Correct!")
else:
	while (str(Guess_number) != str(Random_number)):
		print("Wrong, try again!")
		Guess_number = input("Guess the number: ")
	else:
		print("Correct!")
		

		
