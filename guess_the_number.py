import random

#stores the levels of the game. 
levels = {
    "e":5,
    "i":10,
    "h":5
}

# checks to see if user input is numerical.
def check_num(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            print("Invalid Input. Please select a number next time.")

def check_level(prompt):
    while True:
        try: 
            return input(prompt) in levels
        except ValueError:
            print("incorrect")
            

check_level("--->")

def start(): 
    print("Welcome to the number guesing game!!\n")

    user_num = check_num("What would you like the upper range of your game to be?: \n"
              "Ex. If input is '100' then the number will range from 1 to 100.\n" 
              "---> ")
    print(f"I am thinking of a number between 1 and {user_num}")
    difficulty = input("Choose a difficulty: Type 'e' for easy, 'i' for intermediate, 'h' for hard")
    
    
    