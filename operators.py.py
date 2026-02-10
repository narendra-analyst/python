#arithmetic operators are known as (+,-,*,/,%,**)
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
#assignment operators are known as (=,+=,-=,*=,/=) = known as assigning some value as (a = 10)
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
 #comparison / relational operators are known as (==,!=,>,<,>=,<=) != is known as not equal to and it always returns the boolean function (true,false)
n1=15
n2=20
print(n1==n2)
print(n1!=n2)
print(n1>n2)
print(n1<n2)
print(n1>=n2)
print(n1<=n2)
#logical operators is known as AND,NOT,OR functions (In AND function both condition should be ture), (In OR function any one conditions should be true), (In NOT function is returns Trus as False, False as True)
#AND Function
print(True and True)
z=3
y=4
print(y>z)
print(y>=z)
print(z<=y)
#OR Function
print(True or False)
print(z>y)
print(z<=y)
#NOT Function
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

