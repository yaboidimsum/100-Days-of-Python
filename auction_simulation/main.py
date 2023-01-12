from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
end_of_bid = False
bidders = {}

def find_highest_bidders(bidders):
  b = 0
  for key in bidders:
    if bidders[key] > b:
      a = key
      b = bidders[key]
  
  print(f"The winner is {a} with a bid of ${b}")
    
while not end_of_bid:
  name = input("What's your name: ")
  bid_price = int(input("What's your bid: $"))
  bidders[name] = bid_price
  decision = input("Are there any bidders? Type 'yes' or 'no'")

  if decision == "no":
    end_of_bid = True
  clear()

print(bidders)

find_highest_bidders(bidders)

    
