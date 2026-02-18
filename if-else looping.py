# 1.Write a program to count the number of vowels in a given string.
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
        count = count + 1
    else:
        pass
    print("Number of vowels:", count)

# 2.Write a program to reverse a string using a loop (without using slicing).
text =  input("enter a string:")
rev = ""
for ch in text:
    rev = ch + rev
    print("reversed string",rev)

# 3.Write a program to check if a string is a palindrome using a loop.
text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev
if text == rev:
    print("It is a palindrome")
else:
    print("Not a palindrome")

# 4.Write a program to count the number of uppercase and lowercase letters in a string.
text = input("Enter a string: ")
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    else:
        pass  
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
