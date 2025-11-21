import random

print("Welcome to the Number Guessing Game!")

max_number = 100
max_attempts = 5
secret_number = random.randint(1, max_number)

print(f"You have {max_attempts} attempts to guess a number between 1-{max_number}")

for attempt in range(1, max_attempts + 1):
	try:
		guess = int(input(f"\nAttempt#{attempt} Guess a number: "))
	except ValueError:
		print("Enter a valid integer.")
		continue

	if guess > secret_number:
		print("\nToo High")
	elif guess < secret_number:
		print("\nToo Low")
	else:
		print(f"You're correct {secret_number} was the number!")
		break
else:
	print(f"Game over! The number was {secret_number}.")
