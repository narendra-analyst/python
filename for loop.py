# Types of keywords in for loop :
# pass - acts as a placeholder that does nothing
for i in range(5) :
 if i == 2:
  pass

#  break - exists the loop entierly
for i in range(10):
 if i== 2:
   break
 print(i)
# or
for i in range(10):
 if i == 2:
  print(i)
 break
 
# continue - skips the current iteration and moves to next one
for i in range (5):
 if i == 2:
  continue
 print(i)
 
# Types of keywords in For Loop:
# Pass - Acts as a placeholder that does nothing.
for i in range(10) :
   pass

# Break - Exists the loop entierly.
for i in range(5):
   if i == 2:
      break
   print(i)

# Continue - Skips the current iteration and moves to next one.
for i in range(5):
   if i ==2:
      continue
   print(i)

# 1.Write a program to print numbers from 1 to 10 using a for loop.
for i in range (1,10):
  print(i)

# 2. Write a program to print even numbers from 1 to 20 using a for loop.
for even in range (1,20):
  if even %2==0 : 
   print(even)

# 3. Write a program to print odd numbers from 1 to 20 using a for loop.
for odd in range (1,20):
  if odd %2!=0:
    print(odd)

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

# 8.Write a program to find the sum of even numbers from 1 to 20.
total = 0
for even in range(1, 11):
    total = total + even
    if total %2 == 0 :
        print("sum =",total)

# 9.Write a program to find the sum of odd numbers from 1 to 20.
total = 0
for odd in range(1, 11) :
    total = total + odd
    if total %2 !=0 :
        print("sum=", total)

# 10.Write a program to print the multiplication table of 7.
for i in range(1,11):
    print(7*i)

# 11.Write a program to print numbers divisible by 3 from 1 to 30.
for i in range (1,30):
    if i %3 == 0 :
        print(i)

# 12.Write a program to find the factorial of 5 using a for loop.
fact = 1
for i in range(1,6):
    fact = fact * i
    print("factorial=",fact)

# 13.Write a program to print numbers from 1 to n (take any fixed n like 15).
n = 15
for i in range(1,n+1):
    print(i)

# 14.Write a program to count the digits of a number (example: 54321).
num = 54321
count = len(str(num))
print("digits=",count)

# 15.Write a program to reverse a number using a for loop (example: 1234 → 4321).
for i in range (4,0,-1):
  print(i)

# 16.Write a program to print the digits of a number (example: 987 → 9, 8, 7).
num = 987
for digits in str(num):
 print(digits)

# 17.Write a program to find the sum of digits of a number (example: 564 → 15).
num = 564
total = 0
for digit in str(num):
    total += int(digit)
print("Sum =", total)

# 18.Write a program to calculate power of a number using loops (example: 2⁵).
base = 2
power = 5
result = 1
for i in range(power):
    result = result * base
    print("Answer =", result)

# 19. Write a program to check if a number is prime or not using a for loop.
num = 3
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            if is_prime:
             print("Prime number")
    else:
      print("Not a prime number")

# 20.Write a program to print a right-triangle star pattern using a for loop.
rows = 5 
for i in range(1, rows + 1):
    print("*" * i)