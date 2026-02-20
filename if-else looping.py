# 1.Write a program to count the number of vowels in a given string.
# text = "vijay"
# count = 0
# for ch in text:
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
#         count = count + 1
#     else:
#         pass
# print("Number of vowels:", count)

# # 2.Write a program to reverse a string using a loop (without using slicing).
# text =  "narendra"
# rev = ""
# for ch in text:
#     rev = ch + rev
# print(rev)

# # 3.Write a program to check if a string is a palindrome using a loop.
# text = "mom"
# rev = ""
# for ch in text:
#     rev = ch + rev
# if text == rev:
#     print("It is a palindrome")
# else:
#     print("Not a palindrome")

# # 4.Write a program to count the number of uppercase and lowercase letters in a string.
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

# #5. Write a program to remove all spaces from a string without using built-in replace().
# text = "Lorem Ipsum is simply dummy text"
# result = ""
# for ch in text:
#     if ch != " ":
#         result += ch
# print(result)

# # 6.Write a program to find the frequency of each character in a string.
# text ="narenda stark"   
# frequency = {}
# for ch in text:
#     if ch in frequency:
#         frequency [ch] += 1
#     else:
#         frequency [ch] = 1
# for key , value in frequency.items():
#    print(key,":",value)

# # 7. Write a program to count how many digits are present in a string.
# text = "narendra0615"
# count = 0
# for ch in text:
#     if ch.isdigit():
#         count += 1
# print("Total digits:", count)

# # 8.Write a program to check if a string contains only alphabetic characters (without using isalpha()).
text = "tonystark15"
only_alpha = True
for ch in text:
    if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z'):
        only_alpha = False
print("Only alphabets:", only_alpha)

# text = "narendra15"
# for ch in range(1):
#  if text == text :
#   print("it contians only alphabet")
# else:
#  print("it not contains only alphabet")
    






# # 9.Write a program to convert all lowercase letters in a string to uppercase manually using ASCII values.
# text = "narendra"
# stringUpper = text.upper()
# print(stringUpper)
# for ch in text :
#     if ch.upper():
        
# # 10.Write a program to print all characters located at even indices of a string
# text = "narendra"
# for i in range(len(text)) :
#     if i %2 == 0 :
#         print(text[i])

# # 11.Write a program to count the number of words in a string without using split().


# # 12.Write a program to replace all vowels in a string with * using a loop.
# text = "thalapthy vetri kondan"
# result = ""
# for ch in str(text):
#     if ch in "aeiou":
#           result += "*"
#     else:
#         result += ch
# print(result)

# 13.

# 14.

# 15.
# text = "narendra@15"
# count = 0
# for ch in text :
#     if ch in "@#$*":
#         count += 0
#     print("special character:",count)

# 16.

# 17.


# 18.Write a program to count the number of consonants in a given string.
# text = "jana nayagan"
# count = 0
# for ch in text:
#     if ch.isalpha() and ch not in "aeiou":
#         count += 1
# print("Consonants:", count)

# 19.


# 20.