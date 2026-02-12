lower = int(input("Enter the lower bound of the interval:"))
higher = int(input("Enter the upper bound of the interval:"))
print(f"Armstrong numbers between {lower} and {higher} are:")
for num in range(lower,higher + 1):
  num_str = str(num)
  num_digits = len(num_str)
  sum = 0
  temp_num = num
  while temp_num > 0:
    digit = temp_num % 10
    sum += digit**num_digits
    temp_num //= 10
  if sum == num:
    print(num)
  