#While Loop
# A while loop in python is a control statement flow statement that repeatedly executes a block of code as long as a specified condition remains 'True'.
# syntax for while loop
# while condition :
#    //code
# Examples 1:
# i = 1
# while i<= 10:
#     if i %2==0:
#      print(i)
#     i += 1

# # Example 2:
# i = 1
# while i<= 10:
#      print(i)
#      i += 1

# 1.Write a program to print numbers from 1 to 10 using a while loop.
i = 1
count = 10
while i <= count :
   print(i)
   i += 1

# 2.Write a program to print even numbers from 1 to 10 using a while loop.
i = 1
count = 10
while i <= count :
   if i %2 == 0 :
      print(i)
   i += 1

# 3. Write a program to print odd numbers from 1 to 20 using a while loop.
i = 1
count = 10
while i <= count :
   if i %2 != 0 :
      print(i)
   i += 1

# 4.Write a program to find the sum of even numbers from 1 to 20 using while loop.
num = 1
total = 0
while num <= 10:
    if num % 2 == 0:
        total = total + num
    num = num + 1
print(total)

# 5.Write a program to print numbers divisible by 3 from 1 to 30 using while loop.
i = 1
count = 30
while i <=30 :
    if i %3 == 0 :
        print(i)
    i += 1

# 6.Write a program to find the factorial of 5 using a while loop.
i = 1
fact = 1
while i <= 5:
    fact = fact * i
    i += 1
print(fact)
