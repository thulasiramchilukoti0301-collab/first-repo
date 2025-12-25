while True:
  try:
    x=int(input("Enter a number: "))
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
  else:
    break
print(f"x is {x}")