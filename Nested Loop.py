# #1.Star Square Pattern
row = 5
for i in range(row):
    for j in range(row):
        print("*",end=" ")
    print()

# #2.Right Triangle Star Pattern
row = 3
for i in range(3):
    for j in range(i+1):
        print("*",end=" ")
    print()

# #3.Inverted Right Triangle
n = 4
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# #4.Pyramid Pattern
n = 4
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(i):
        print("* ", end="")
    print()

# #5.Number Triangle Pattern
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# #6.Floyd’s Triangle
n = 4
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# #7.Diamond Pattern
n = 4

#8.Upper part
n = 5
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* " * i)

#9.Lower part
n = 5
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    print("* " * i)