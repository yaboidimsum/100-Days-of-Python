from art import logo
#Calculator

#Add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

print(logo)

def calculator():
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)

  
  should_continue = True #Flag
  
  while should_continue:  
    operation_symbol = input("Pick another operation: ")
    num2 = float(input("What's the next number?: "))
    calculator_function = operations[operation_symbol]
    answer = calculator_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
    if decision == "n":
      should_continue = False
      calculator()
    else:
      num1 = answer

calculator()
