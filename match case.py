# 1.Write a program to check whether a number is *even or odd* using match.
num=int(input('enter a value:'))
match num %2 :
    case 0 :
        print('even number')
    case 1 :
        print('odd number')
    case _ :
        print('default is working')
# 2.Write a program to check whether a number is *positive, negative, or zero* using match.
num=int(input('enter a value:'))
match num :
    case n if n > 0 :
        print('postive number')
    case n if n < 0 :
        print('negative number')
    case n if n == 0 :
        print('it is zero')
    case _ :
        print('default is working')
# 3.Create a *simple calculator* that performs addition, subtraction, multiplication, or division based on user input using match.
amount1 = float(input('enter a total amount1:'))
amount2 = float(input('enter a total amount2:'))
operator = input('enter operator (+,-,*,/):')
match operator :
    case '+' :
        print('result=',amount1 + amount2)
    case '-' :
       print('result=',amount1 - amount2)
    case '*' :
        print('result=',amount1 * amount2)
    case '/' :
        print('result=',amount1 / amount2)
    case _ :
        print('default is working')
# 4.Write a program to check whether a given day is a *weekday or weekend* using match.
day=str(input('enter a day:')).lower()
match day :
    case 'saturday'|'sunday' :
        print('it is a weekend')
    case 'monday'|'tuesday'|'wednesday'|'thursday'|'friday' :
        print('it is a weekday')
    case _ :
        print('default is working')
# 5.Write a program to implement a *grading system* based on marks (A, B, C, D, Fail) using match
mark=int(input('enter your mark:'))
match mark :
    case n if n > 80 :
        print('your grade is A')
    case n if n > 70 :
        print('your grade is B')
    case n if n > 60 :
        print('your grade is C')
    case n if n > 50 :
        print('your grade is D')
    case n if n > 40 :
        print('your grade is E')
    case n if n < 40 :
        print('your grade is F')
    case _ :
        print('default is working')
# 6. Write a program to display the *month name* based on a given month number (1–12) using match.
month=int(input('enter the month number:'))
match month :
    case month if month == 1 :
        print('janauary month')
    case month if month == 2:
        print('february month')
    case month if month == 3 :
        print('march month')
    case month if month == 4:
        print('april month')
    case month if month == 5 :
        print('may month')
    case month if month == 6:
        print('june month')
    case month if month == 7 :
        print('july month')
    case month if month == 8:
        print('august month')
    case month if month == 9 :
        print('september month')
    case month if month == 10:
        print('october month')
    case month if month == 11 :
        print('november month')
    case month if month == 12:
        print('december month')
    case _ :
        print('default is working')
#7. Write a program to check whether a character is a *vowel or consonant* using match.
ch=str(input('enter a character:')).lower()
match ch :
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('it is vowel')
    case 'b' | 'c' | 'd' | 'f' | 'g':
        print('it is consonant')
    case _ :
        print('default is working')
# 8.Write a program to print action based on a *traffic signal color* (Red, Yellow, Green) using match.
traffic=str(input('enter a signal action:'))
match traffic:
    case traffic if traffic == 'stop' :
        print('signal color is red')
    case traffic if traffic == 'ready' :
        print('signal color is yellow')
    case traffic if traffic == 'go' :
        print('signal color is green')
    case _ :
        print('default is working')           
# 9.Write a program to check whether a given year is a *leap year* using match.
year=int(input('enter the total number of days in feburary:'))
match year :
    case 28 :
        print('this is leap year')
    case 29 :
        print('this is non leap year')
    case _ :
        print('default is working')
# 10.Write a program to categorize a person based on *age group* (Child, Teen, Adult, Senior) using match.
age=int(input('enter your age:'))
match age :
    case age if age < 14:
        print('your are a child')
    case age if age < 18 :
        print('your are a teen')
    case age if age < 60 :
        print('your are a adult')
    case _ :
        print('your are a senior')
# 11.Write a program to check whether a number lies *between 1 and 10* using match.
num=int(input('enter a number:'))
match num :
    case num if num <=10 :
        print('yes this number lies between 1 and 10')
    case _ :
        print('default is working')
# 12.Write a program to validate a *username and password* using match.
userName = 'narendra'
userPassword = 'narendra@15'
ch1=str(input('enter username:'))
ch2=str(input('enter userpassword:'))
match (ch1 , ch2) :
    case ('narendra' , 'narendra@15') :
        print('login successful')
    case ('narendra' , _) :
        print('password incorrect')
    case _ :
        print('invalid username and password')
# 13.Write a program to identify a *shape name* based on the number of sides using match.
sides=int(input('enter the number of sides:'))
match sides :
    case 3 :
        print('Triangle')
    case 4 :
        print('Quadrilateral')
    case 5 :
        print('Pentagon')
    case 6 :
        print('Hexagon')
    case _ :
        print('default is working')
# 14.Write a program to check whether a number is *divisible by both 3 and 5* using match.
num=int(input('enter a value is divisible by 3 and 5:'))
match num :
    case num if num %3 %5 == 0 :
        print('it is divisble by 3 and 5')
    case num if num %3 %5 !=0 :
        print('it is not divisble by 3 and 5')
    case _ :
        print('default is working')
# 15.Write a program to classify a number as *Positive Even, Positive Odd, Zero, or Negative* using match.
num=int(input('enter a number:'))
match num :
    case num if num>0 and num %2 == 0 :
        print('postive even number')
    case num if num>0 and num %2 != 0 :
        print('postive odd number')
    case num if num < 0 :
        print('negative number')
    case _ :
        print('default is working')


num = int(input("enter a value:"))
match num :
    case _ if num > 0 :
        print ("positive")
    case _ if num < 0 :
        print("odd")
    case _ :
        print("zero")

