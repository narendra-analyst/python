# 1.Write a program to count the number of vowels in a given string.
# text = "vijay"
# count = 0
# for ch in text:
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
#         count = count + 1
#     else:
#         pass
# print(count)

# 2.Write a program to reverse a string using a loop (without using slicing).
# text =  "narendra"
# rev = ""
# for ch in text:
#     rev = ch + rev
# print(rev)

# 3.Write a program to check if a string is a palindrome using a loop.
# text = "mom"
# rev = ""
# for ch in text:
#     rev = ch + rev
# if text == rev:
#     print("It is a palindrome")
# else:
#     print("Not a palindrome")

# 4.Write a program to count the number of uppercase and lowercase letters in a string.
# text = "Stark"
# upper = 0
# lower = 0
# for ch in text:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     else:
#         pass  
# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)

#5. Write a program to remove all spaces from a string without using built-in replace().
# text = "Lorem Ipsum is simply dummy text"
# result = ""
# for ch in text:
#     if ch != " ":
#         result += ch
# print(result)

# 6.Write a program to find the frequency of each character in a string.
# text ="narenda stark"   
# frequency = {}
# for ch in text:
#     if ch in frequency:
#         frequency [ch] += 1
#     else:
#         frequency [ch] = 1
# for key , value in frequency.items():
#    print(key,":",value)
# # or
# text = "narendra"
# for ch in text:
#     print(ch, "=", text.count(ch))

# 7. Write a program to count how many digits are present in a string.
text = "narendra0615"
digits = 0
for digits in text:
    if digits :
        result += digits
print(digits)

text = "narendra0615"

count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print("Total digits:", count)
