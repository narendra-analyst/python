# implicit - automatically convert one type to another
#int
a=15
b=22
c=a+b
print(c)
print(type(c))

#boolean
x=True
y=False
print(x)
print(type(x))

#string
num="50"
print(type(num))

# explicit - manually convert one type to another
#inttostr
d=25
InttoStr=str(d)
print(type(InttoStr))

#strtoint
e="45"
StrtoInt=int(e)
print(type(StrtoInt))

#boolntoint
x=True
boolntoint=int(x)
print(type(boolntoint))

#inttobooln
y=False
inttobooln=bool(y)
print(type(inttobooln))

#boolntostr
z=True
boolntostr=str(z)
print(type(boolntostr))

#strtobooln
n="True"
strtobooln=bool(n)
print(type(strtobooln))

#listtotuple
myList=[1,2,3,4,5,6]
listtotuple=tuple(myList)
print(type(listtotuple))

#tupletolist
myTuple=(20,30,40)
tupletolist=list(myTuple)
print(type(tupletolist))

#tupletoset
myTuple=(20,30,40)
tupletoset=set(myTuple)
print(type(tupletoset))

#settotuple
mySet={50,"name",18.5}
settotuple=tuple(mySet)
print(type(settotuple))
