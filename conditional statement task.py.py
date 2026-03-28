#conditional statement- if and else, in this statement it always recieves only string value wether we enter integer or string in the variable, because it is as default string value only.
# Examples:
age = 21
if age >= 18:
   print("eligible to vote")
else:
   print("Not eligible to vote")

n = int(input("Enter n value: "))
if n>= 0:
    print("+ve")
else:
    print("-ve")

userName = input("Enter your name : ")
print(userName)

shop1 = input("Enter your total bill amount in shop1: ")
shop2 = input("Enter your total bill amount in shop2: ")
print(shop1)
print(shop2)

totalAmountToPay = int(shop1) + int(shop2)
print(totalAmountToPay)

# Task:
#1.Check even or odd
num = 16
if num %2 == 0 :
    print("even")
else:
    print("odd")

#2.Check positive or negative
n = 10
if n >= 0 :
    print("+ve")
else:
    print("-ve")

#3.Check eligible to vote
name = 28 
if name >= 18 :
    print("eligible to vote")
else :
    print("not eligible to vote")

#4.Find greater of two numbers.
a = 20
b = 10
if a > b:
    print("greater number is",a)
else :
    print("greater number is",b)

#5.Check divisible by 5
num = 48
if num  % 5 == 0 :
    print("48 is divisible by 5")
else :
    print("48 is not divisble by 5")

#6.Check pass or fail
narendra = 98
if narendra >= 35 :
    print("yes narendra is pass")
else :
    print("no narendra is fail")

#7.Check number is two-digit
number = 22
if number == 22 :
    print("yes 22 is a two digit number")
else :
    print("no 22 is not a two digit number")

#8.Check divisible by 10
num = 50
if num  % 10 == 0 :
    print("50 is divisible by 10")
else :
    print("50 is not divisible by 10")

#9.Check number greater than 100
value = 560
if value >= 100 :
    print("560 is greater than 100")
else :
    print("560 is not greater than 100")

#10.Check vowel or consonant
ch = 'a','e','i','o','u'
if ch == ('a','e','i','o','u') :
    print("it is vowel")
else :
    print("it is consonant")

#11.Check number divisible by 2 and 3
num = 6
if num %2 %3 == 0 :
    print("6 is divisible by 2 and 3")
else :
    print("6 is not divisible by 2 and 3")

#12.Check number is zero or non-zero
number = 35
if number == 0 :
    print("yes number is zero")
else :
    print("number is non-zero")

#13.Check number less than 5
number = 3.5
if number < 5 :
    print("yes 3.5 is less than 5")
else :
    print("no 3.5 is not less than 5")

    

