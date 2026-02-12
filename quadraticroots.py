import math
a=int(input("Enter coefficient a: "))
b=int(input("Enter coefficient b: "))
c=int(input("Enter coefficient c: "))
D=b**2-4*a*c
if D>0:
  root1=(-b+math.sqrt(D))/2*a
  root2=(-b-math.sqrt(D))/2*a
  print("Roots are real and different")
  print("Root 1:",root1)
  print("Root 2:",root2)
if D == 0:
  root=(-b)/(2*a)
  print("Roots are real and same")
  print("Root:",root)
if D<0:
  realpart=-b/(2*a)
  imagpart=math.sqrt(abs(D))/(2*a)
  print("Roots are complex and different")
  print("Root 1:",realpart,"+",imagpart,"i")
  print("Root 2:",realpart,"-",imagpart,"i")