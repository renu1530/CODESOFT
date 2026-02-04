# calculator using python

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  if b == 0:
    return "zero division error"

  return a / b



while True:

  print('----- Calculator -----')
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")

  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  if choice in (1, 2, 3, 4):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if choice == 1:
      print("Result:", add(num1, num2))

    elif choice == 2:
      print("Result:", sub(num1, num2))

    elif choice == 3:
      print("Result:", mul(num1, num2))

    elif choice == 4:
      print("Result:", div(num1, num2))

  elif choice == 5:
    print("Exiting the calculator")
    break

  else:
    print("Invalid choice. Please try again.")





