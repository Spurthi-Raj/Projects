import random
number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number between 1 and 100 : '))
        if guess < 1:
            print("Enter positive number")
        elif guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! you guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")

