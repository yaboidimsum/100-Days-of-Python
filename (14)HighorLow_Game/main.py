from art import logo,vs
from game_data import data
import random
from replit import clear

print(logo)

def random_data():
  return random.choice(data)

def format_data(account):
  name = account ["name"]
  description = account ["description"]
  country = account ["country"]
  return f"{name},a {description},from {country}"

def check_score(guess,data_a,data_b):
  a = data_a["follower_count"]
  b = data_b["follower_count"]
  if a > b:
    return guess == "a"
  else:
    return guess == "b"
  

# def score_compare():

def game():
  score = 0
  end_of_game = False
  statement_a = random_data()
  statement_b = random_data()

  while not end_of_game:
    statement_a = statement_b
    statement_b = random_data()

    while statement_a == statement_b:
      statement_b = random_data

    print(format_data(statement_a))
    print(vs)
    print(format_data(statement_b))
    guess = input("Who has more follower? Type 'A' or 'B: '").lower()

    is_correct = check_score(guess,statement_a,statement_b)
    
    clear()
    print(logo)

    if is_correct:
      score += 1
      print(f"You are right! You're point is {score}")
    else:
      end_of_game = True
      print(f"You lose! You're final point is {score}")
    
game()
  

