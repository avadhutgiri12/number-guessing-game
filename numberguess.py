import random

computer = random.randint(1,100)



print('''Choose Difficulty Level:
      1.Easy (10 Chances)
      2.Medium (5 Chances)
      3.Hard (3 Chances)''')

level = int(input("Enter Your choice: "))

def game():
       user = int(input("Enter Your Guess :"))

       if computer > user:
              print("The Number is greater than your!")

       elif computer < user:
              print("The Number is smaller than your!")

       elif computer == user:
              print(f"You win! Your Guess is correct :{user}")
              exit()


def chance():
       if (level == 1):
              for i in range(1,11):
                     game()
       if (level == 2):
              for i in range(1,6):
                     game()
       if (level == 3):
              for i in range(1,4):
                     game()

chance()