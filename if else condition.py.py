#conditional statement- if and else, in this statement it always recieves only string value 
#1.Check even or odd
num = int(input (" entre a value:"))
if num %2 == 0 :
    print("even")
else:
    print("odd")
    
#2.Check positive or negative
n = int(input("entre n value:"))
if n >= 0 :
    print("+ve")
else:
    print("-ve")
    
#3.Check eligible to vote
age = int(input('entre your age:'))
if age >= 18 :
    print("eligible to vote")
else :
    print("not eligible to vote")
    
#4.Find greater of two numbers
a = 20
b = 10
c = input('entre a lesser than value:')
if a > b:
    print("greater number is",a)
else :
    print("greater number is",b)
    
#5.Check divisible by 5
num = int(input('entre a 5 divisible value:'))
if num  % 5 == 0 :
    print("48 is divisible by 5")
else :
    print("48 is not divisble by 5")
    
#6.Check pass or fail
narendra = int(input('entre your mark:'))
if narendra >= 35 :
    print("yes narendra is pass")
else :
    print("no narendra is fail")
    
#7.Check number is two-digit
number = int(input('entre a two digit number:'))
if number == 22 :
    print("yes 22 is a two digit number")
else :
    print("no 22 is not a two digit number")

#8.Check divisible by 10
num = int(input('entre a 10 divisible value:'))
if num  % 10 == 0 :
    print("50 is divisible by 10")
else :
    print("50 is not divisible by 10")

#9.Check number greater than 100
value = int(input('entre a number greater than 100:'))
if value >= 100 :
    print("560 is greater than 100")
else :
    print("560 is not greater than 100")

#10.Check vowel or consonant
ch = str(input('entre a vowel character:'))
if ch == ('a','e','i','o','u') :
    print("it is vowel")
else :
    print("it is consonant")

#11.Check number divisible by 2 and 3
num = int(input('entre a number divisible by 2 and 3:'))
if num %2 %3 == 0 :
    print("6 is divisible by 2 and 3")
else :
    print("6 is not divisible by 2 and 3")

#12.Check number is zero or non-zero
number = int(input('entre a  zero or non-zero number:'))
if number == 0 :
    print("yes number is zero")
else :
    print("number is non-zero")

#13.Check number less than 5
number = int(input('entre a number less than 5:'))
if number < 5 :
    print("yes 3 is less than 5")
else :
    print("no 3 is not less than 5")

