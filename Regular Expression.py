# Regular Expression (Regex):
# Regular Expression (often called regex) in Python is a powerful tool to search, match, and manipulate text.

# 1.Why regex is used (in real data analyst work)
# Find specific patterns in data (emails, phone numbers)
# Clean messy text data
# Extract useful information from strings
# Validate inputs (like checking email format)

# 2.Python module for regex
# In Python, we use the built-in module:
# import re

# Basic Example
import re
text = "My number is 8610347810"
result = re.search(r"\d+", text)
print(result.group())

# Important Functions in regex:

# 1. re.search()
# Finds first match
# re.search(pattern, text)

# 2.re.findall()
# Finds all matches
text = "My marks: 45, 67, 89"
print(re.findall(r"\d+", text))

# 3.re.sub()
# Replace text
text = "I like apple"
print(re.sub("apple", "banana", text))

# 4.re.split()
# Because real data is messy Sometimes separators are mixed.
import re
text = "abc123xyz456"
print(re.split(r"\d+", text))

# Common Regex Patterns (Very Important)
# Pattern	Meaning	                    Example
# \d	    digit                       (0–9)	5
# \D	    not digit	                a
# \w	    word (a-z, A-Z, 0-9, _)	    name_1
# \W	    not word	                @
# \s	    space	                    " "
# .	        any character	            a, 1, @
# ^	        start of string	            ^Hello
# $	        end of string	            end$
# +	        one or more	                \d+
# *	        zero or more	            a*

  