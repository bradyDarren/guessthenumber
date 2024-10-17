import random
from art import logo

#stores the levels of the game. 
levels = {
    "e":5,
    "i":10,
    "h":15
}

# checks to see if user input is numerical.
def check_num(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            print("Invalid Input. Please select a number next time.")

# checks to see if user input is within the provided selections. 
def check_level():
    while True:
        difficulty = input("Choose a difficulty: Type 'e' for easy, 'i' for intermediate, 'h' for hard: ")
        if difficulty not in levels: 
            print("Invalid Selection. Please make an appropriate selection from the given choices.")
        else: 
            return difficulty          

def start():
    print(logo)

    print("Welcome to the number guesing game!!\n")

    user_num = check_num("What would you like the upper range of your game to be?: \n"
              "Ex. If input is '100' then the number will range from 1 to 100.\n" 
              "---> ")
    print(f"I am thinking of a number between 1 and {user_num}")
    rand_num = random.randrange(user_num)
    # print(rand_num) - test line
    user_level = levels[check_level()]
    while user_level != 0:
        user_guess = check_num("Make a guess: ")
        if user_guess > rand_num:
            print("Too High") 
            user_level -= 1
            print(user_level)
        elif user_guess < rand_num:
            print("Too Low")
            user_level -= 1
        elif user_guess == rand_num:
            print("You have guessed correctly!!!")
    
    if user_level == 0:
        print("You lose. No guesses are remaining.")
start()
    
    
    