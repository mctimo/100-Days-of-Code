rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)
else:
    print("Invalid choice")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if choice == str(computer_choice):
    print(f"It's a tie! The computer chose {computer_choice}")
elif choice == "0" and computer_choice == 1:
    print("You lose! Paper beats rock")
elif choice == "0" and computer_choice == 2:
    print("You win! Rock beats scissors")
elif choice == "1" and computer_choice == 0:
    print("You win! Paper beats rock")
elif choice == "1" and computer_choice == 2:
    print("You lose! Scissors beats paper")
elif choice == "2" and computer_choice == 0:
    print("You lose! Rock beats scissors")
elif choice == "2" and computer_choice == 1:
    print("You win! Scissors beats paper")
