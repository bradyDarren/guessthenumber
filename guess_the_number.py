import random
from art import logo

#stores the levels of the game. 
levels = {
    "e":12,
    "i":8,
    "h":4
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
    remaining_turns = user_level
    while remaining_turns != 0:
        user_guess = check_num("Make a guess: ")
        if user_guess > rand_num:
            print("Too High") 
            remaining_turns -= 1
            # print(remaining_turns) - test line
        elif user_guess < rand_num:
            print("Too Low")
            remaining_turns -= 1
            # print(remaining_turns) - test line
        elif user_guess == rand_num:
            print("You have guessed correctly!!!")
            break
    
    if remaining_turns == 0:
        print("You lose. No guesses are remaining.")
start()
    