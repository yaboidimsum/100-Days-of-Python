import random

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

weapon = [rock, paper, scissors]
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_option = random.randint(0, 2)
computer = weapon[computer_option]

if human >= 3 and human < 0:
    print("Your input is incorrect. You lose")
elif human == 0 and computer_option == 2:
    print(weapon[human] + "Computer chose:\n" + computer + "\nYou win")
elif human == 2 and computer_option == 0:
    print(weapon[human] + "Computer chose:\n" + computer + "\nYou lose")
elif human > computer_option:
    print(weapon[human] + "Computer chose:\n" + computer + "\nYou win")
elif human < computer_option:
    print(weapon[human] + "\nComputer chose:\n" + computer + "\nYou lose")
else:
    print(weapon[human] + "\nComputer chose:\n" + computer + "\nDraw")
