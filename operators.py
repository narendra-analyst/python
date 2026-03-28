#arithmetic operators ( +,-,*,/,**) square value (**)
a,b = 149,199
print(a+b)

#membership operators (in , not in)
myList=[10,20,30,40,50,60]
print(40 in myList, "membership")
print(20 not in myList, "membersip")

#identity operators (is, is not)
department1=["CSE","IT","ECE","EEE"]
department2=["CSE","IT","ECE","EEE"]
name1="narendra"
name2="narendra"
num1=15
num2=9
department3=department2
num3=name1
print(department1 is department2)
print(name1 is name2)
print(num1 is not num2)
print(department2 is department3)
print(name1 is num3)


shop1 = input('entre your total bill amount in shop1:')
shop2 = input('entre your total bill amount in shop2:')
print(shop1)
print(shop2)
totalAmoutnToPay=int(shop1)+int(shop2)
print(totalAmoutnToPay)

# bitwise operator
print(10 & 15)

# arithmetic operators are known as (+,-,*,/,%,**)
a,b=15,20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
c=4
print(c**2)
print(2**5)

# assignment operators are known as (=,+=,-=,*=,/=) = known as assigning some value as (a = 10)
x=20
x+=10
print(x)
x-=10
print(x)
x/=2
print(x)
x*=2
print(x)
x%=2
print(x)

# comparison / relational operators are known as (==,!=,>,<,>=,<=) != is known as not equal to and it always returns the boolean function (true,false)
n1=15
n2=20
print(n1==n2)
print(n1!=n2)
print(n1>n2)
print(n1<n2)
print(n1>=n2)
print(n1<=n2)

# logical operators is known as AND,NOT,OR functions (In AND function both condition should be ture), (In OR function any one conditions should be true), (In NOT function is returns Trus as False, False as True)
# AND Function
print(True and True)
z=3
y=4
print(y>z)
print(y>=z)
print(z<=y)

# OR Function
print(True or False)
print(z>y)
print(z<=y)

# NOT Function
print(not True)
print(not(y<z))

# membership operator - ( in, not in)
myList = [1,2,3,4,5,6]
print(5 in myList,"Membership")
print("aaa" in myList,"member")
print(3 not in myList)

# identity operator - ( is, is not)
department1 = ["CSE","IT","ECE"]
department2 = ["CSE","IT","ECE"]
print( department1 is department2)   # False
department3 = department2
print( department3 is department2)   #  true

# bitwise operator
print(20&30)
print(10&15)
