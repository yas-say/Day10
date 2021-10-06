from art import logo
from replit import clear

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b




operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

def mycalc():
  clear()
  print(logo)
  num1 = float(input("What's the first number?: "))
  isTrue = True

  while isTrue:
    print("Available Operators: ")
    for o in operations:
      print(o)
    chosen = input("Choose one of them: ")
    num2 = float(input("What's the next number?: "))
    n = operations[chosen](num1, num2)
    print(f"{num1} {chosen} {num2} = {n}")
    flag = input(f"Type 'y' to continue calculating with {n}, or type 'n' to get new numbers, or 'x' to exit: ").lower()
    num1 = n
    if flag == 'y':
      isTrue = True
    elif flag == 'n':
      mycalc()
    else:
      print("Existing")
      return

mycalc()
