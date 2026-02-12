#elif condition:
#1.Check if a number is +ve,-ve or 0?
num = int(input('enter a number:'))
if num>10 :
   print('it is a +ve number')
elif num<10:
   print('it is a -ve number')
else:
   print('it is a zero')
#2.Find the greatest of three numbers
a = int(input('enter A value:'))
b = int(input('enter B value:'))
c = int(input('enter C vlaue:'))
if (a>b) and (a>c):
   print('greater number is a')
elif (b>a) and (b>c):
   print('greater number is b')
else:
   print('greater number is c')
#3.grade calculator
#99 - 100 - S
#89 - 80 - A
#79 - 70 - B
#69 - 60 - C
#59 - 50 - D
#49 - 40 - E
#39 - 30 - F
mark = int(input('enter your mark:'))
if mark>=90 :
   print('your grade is S')
elif mark>=80 :
   print('your grade is A')
elif mark>=70 :
    print('your grade is B')
elif mark>=60 :
    print('your grade is C')
elif mark>=50 :
    print('your grade is D')
elif mark>=40 :
    print('your grade is E')
else :
   print('your grade is F')
#4.Check if number is zero, even or odd
num=int(input('enter a number:'))
if num==0:
   print('the number is zero')
elif num%2==0:
   print('the number is even')
else:
   print('the number is odd')
#5.Check Type of Triangle (by sides) ( Equilateral Triangle, Isosceles Triangle, Scalene Triangle)
sides=int(input('enter the equal sides :'))
if sides==3:
   print('equilateral triangle')
elif sides==2:
   print('isoceles triangle')
else:
   print('scalene triangle')
#6.Simple calculator (using only conditionals)
amount1=float(input('enter amount1:'))
amount2=float(input('enter amount2:'))
operator=input('enter operator (+,-,*,/):')
if operator =='+':
   print("result=" , amount1+amount2)
elif operator =='-':
   print("result=" , amount1-amount2)
elif operator =='*':
   print("result=" , amount1*amount2)
elif operator =='/':
   print("result=" , amount1/amount2)
else:
 print("invalid operator")

 
