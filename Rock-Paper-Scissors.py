# Rock Paper Scissors
import random
print('Welcome to the Rock-Paper-Scissors game !')
user_choice = int(input('\nType 0 for rock, 1 for paper or 2 for scissors: '))

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print('Unrecognized number, try again !')

computer_choice = random.randint(0, 2)
print(choices[computer_choice])

if user_choice == computer_choice:
    print('It\'s a tie !')
elif ((user_choice == 0 and computer_choice == 2) or
      (user_choice == 1 and computer_choice == 0) or
      (user_choice == 2 and computer_choice == 1)):
    print('You win !')
else:
    print('You lose !')