import random

computer = random.randint(1,100)

print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n''')

print('''Choose Difficulty Level:
      1.Easy (10 Chances)
      2.Medium (5 Chances)
      3.Hard (3 Chances)\n''')

level = int(input("Enter Your choice: "))

def game():
       user = int(input("Enter Your Guess :"))

       if computer > user:
              print(f"Incorrect! The number is less than {user}.")

       elif computer < user:
              print(f"Incorrect! The number is less than {user}.")

       elif computer == user:
              print(f"You win! Your Guess is correct :{user}")
              exit()


def chance():
       if (level == 1):
              print("Great! You have selected the easy difficulty level.\nLet's start the game!")
              for i in range(1,11):
                     game()
       if (level == 2):
              print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
              for i in range(1,6):
                     game()
       if (level == 3):
              print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
              for i in range(1,4):
                     game()

chance()

print("you are boss")