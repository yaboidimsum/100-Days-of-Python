#Password Generator Project
import random,string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for letter in range(0,nr_letters):
  password += letters[random.randint(0,51)]
for symbol in range(0,nr_symbols):
  password += symbols[random.randint(0,8)]
for number in range(0,nr_numbers):
  password += numbers[random.randint(0,9)]

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

randomize_password = ''.join(random.sample(password, len(password)))
print(randomize_password)


# def randomize_string(string):
#   return ''.join(random.sample(string, len(string)))

# randomized_string = randomize_string("Hello, World!")
# print(randomized_string)
#Kalau pakai fungsi
