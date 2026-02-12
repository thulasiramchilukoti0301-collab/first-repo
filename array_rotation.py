def rotate_array(arr,d):
  n = len(arr)
  if d < 0 or d >= n:
    print("invalid rotation value")
  rotated_arr = [0]*n
  for i in range(n):
    rotated_arr[i] = arr[(i + d) % n]
  return rotated_arr
arr = [1,2,3,4,5]
d = int(input("Enter number of positions to rotate: "))
result = rotate_array(arr,d)
print("Original array:", arr)
print("Rotated array:", result) 

    