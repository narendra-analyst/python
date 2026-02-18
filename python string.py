# String Methods
text =" narendra stark"

print("Original:",text)
print("Strip:",text.strip())
print("Upper:",text.upper())
print("Lower:",text.lower())
print("Swapcase:",text.swapcase())
print("Title:",text.title())
print("Capitalize:",text.capitalize())
print("Replace:",text.replace("stark","hero"))
print("Count:",text.count("a"))
print("Index of n:", text.index("n"))
print("Index of s:", text.index("s"))
print("Last character:", text[-1])
print("Second last:", text[-2])

# F-Stirng are used to easily insert variables or expressions inside a string to make output clean and readable.
# Variables
name = "narendra"
age = 28
print(f"I am {name} and I am {age}")

# Expressions
a = 10
b = 20
print(f"sum is {a+b}")

# Variable + Expressions
name = "narendra"
mark = 90
print(f"{name} scored {mark+5} after bonus")

# Simple Decimal 
price = 49.567
print(f"price is {price}")

# Show only two decimals
price = 49.567
print(f"price is {price:.2f}")

# Precentage
score = 0.8567
print(f"score:{score:.2%}")

# selftask
name="narendra"
money= 458.657898789
print(f"{name} spent rupess {money:.2f} today")

# print name and age
name = "narendra"
age = 28
print("f my name is {name} and i am {age} years old")

# city introduction
city = "puducherry"
print(f"i live in {city}")

# favorite food
dish = "dosa"
print(f"my favorite food is {dish}")

# addition take two numbers and print
a = 10
b = 5
print(f"sum is {a+b}")

# multiplication
a = 4
b = 3
print(f"sum is {a*b}")

# square of a number (**)
value = 6
print(f"the square is {6**2}")