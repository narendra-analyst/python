# 1.Write a program to print numbers from 1 to 10 using a for loop.
for i in range (10):
  print(i)

# 2. Write a program to print even numbers from 1 to 20 using a for loop.
for even in range (1,20):
  if even %2==0 : 
   print(even,"numbers")

# 3. Write a program to print odd numbers from 1 to 20 using a for loop.
for odd in range (1,20):
  if odd %2!=0:
    print(odd,"numbers")

# 4.Write a program to print numbers from 10 to 1 in reverse order.
for i in range (10,0,-1):
  print(i)

# 5.Write a program to print the square of each number from 1 to 10.
for i in range (1,11):
  print(i**2)

# 6.Write a program to print the multiples of 5 up to 50.
for i in range (5,51,5):
 print(i)

# 7.Write a program to find the sum of numbers from 1 to 10.
total = 0

for i in range(1, 11):
    total = total + i

print("Sum =", total)
