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
