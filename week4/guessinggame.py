import random 
guesses = 0
a = random.randint(1, 10)
print("Lets Play a Game!  * type exit to leave * ")
print("Guess the Number I'm thinking of from 1 - 10")
while guesses < 10:
        print("Type your guess: ")
        guess = input()
        guess = int(guess)
        guesses = guesses + 1 
        if guess > a:
            print("Too High, try again")
        if guess < a: 
            print("Too Low, try again")
        if guess == a: 
                break 
if guess == a:
    guesses = str(guesses)
    print("Correct, YOU WIN!!!")
    print("Number of guesses: ", guesses)

