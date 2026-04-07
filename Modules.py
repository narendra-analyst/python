# What is Module?
# A module is just a file that contains Python code (functions, variables, classes).
# Instead of writing everything in one file, we divide code into modules.
# eg:
import Modules1
Modules1.greet()

# 1.Why modules are used?
# Reuse code
# Make code organized
# Avoid writing same code again

# Types of Modules in Python:
# 1. Built-in Modules
# These are already available in Python.
# Eg:
# math module → math operations
# random module → random numbers
# datetime module → date & time
# collections module → advanced data structures
import math
print(math.sqrt(16))

# 2. User-defined Modules
# Modules created by you (user).
# Eg:
import Modules1
print(Modules1.add(2, 3))

# 3. Third-party Modules:
# Modules created by others (not built-in).
# Eg:
# pandas
# numpy
# pip install pandas

# Collections module:
# The collections module is a built-in Python module that provides special data types (like advanced versions of list, dict, tuple).
# In simple words:
# It gives you better, smarter containers to store and manage data.

# Types of collections module:
# 1. Counter (Counting made easy)
# Used to count frequency of items
# Eg:
from collections import Counter
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = Counter(data)
print(result)

# It counts how many times each item appears
# Counting words, votes, product sales

# 2.defaultdict  (No key error)
# Like dictionary, but no error for missing key
# defaultdict gives default value (0 here)
# Eg:
from collections import defaultdict
d = defaultdict(int)
d['apple'] += 10
d['banana'] += 20
print(d['cherries'])
print(d)

# Use case: counting, grouping data

# 3.namedtuple (Tuple with names)
# Access values using names instead of index
# Like tuple, but with names (more readable)
# Eg:
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age'])
s = Student('Tony', 28)
print(s.name)
# print(s.age)

# Instead of s[0], you use s.name

# 4.deque (Fast insert/remove)
# FFast list for adding/removing from both sides
# Eg:
from collections import deque
d = deque([1, 2, 3])
d.append(4)        # add right
d.appendleft(0)    # add left
# d.remove(2)
print(d)

# Faster than list for queue operations

# 5.OrderedDict (Keeps order)
# Dictionary that remembers insertion order
# Eg:
from collections import OrderedDict
d = OrderedDict() 
d['a'] = 1
d['b'] = 2
print(d)


# What is random()?
# The random module provides functions to generate random values.
# random() is one of its functions.

# random() Function:
# It gives a random decimal number between 0 and 1
import random
print(random.random())
# Output will change every time you run the program.

# Other Useful Functions in random module
# 1. randint() Random integer
import random
print(random.randint(1, 10))
# Output: any number between 1 and 10

# 2.choice() Pick random item
import random
names = ['a', 'b', 'c']
print(random.choice(names))

# 3.shuffle() Shuffle list
import random
nums = [1, 2, 3, 4]
random.shuffle(nums)
print(nums)

# datetime module:
# What is Date & Time Module?
# In Python, we use the built-in datetime module to work with:
# Current date
# Current time
# Formatting date/time
# Calculating differences between dates

# Main Classes in datetime
# 4 important tools:
# 1. date → Only date (year, month, day)
# 2. time → Only time (hour, minute, second)
# 3. datetime → Both date + time
# 4. timedelta → Difference between two dates

# 1. Get Current Date & Time
from datetime import datetime
now = datetime.now()
print(now)

# 2. Get Only Date
from datetime import date
today = date.today()
print(today)

# 3. Get Only Time
from datetime import datetime
now = datetime.now()
print(now.time())

# 4. Create Your Own Date
from datetime import date
d = date(2026, 4, 6)
print(d)

# 5. Format Date (Very Important)
from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y"))

# 6. Difference Between Two Dates
from datetime import date
d1 = date(2026, 4, 6)
d2 = date(2026, 4, 1)
diff = d1 - d2
print(diff)

# 7. Add Days to Date
from datetime import date, timedelta
today = date.today()
new_date = today + timedelta(days=5)
print(new_date)

# 8.Working with date and time
from datetime import datetime
now = datetime.now()
print(now)       # 2026.4.6 02:31:00
print(now.year)  # 2026
print(now.date)  # 6
print(now.time)  # 02

# Easy Way to Remember
# date → only date
# time → only time
# datetime → both
# timedelta → difference

# Python uses datetime module for date & time
# datetime.now() → current date & time
# date.today() → current date
# strftime() → format date
# timedelta → calculate difference
# Can create custom date using date(YYYY, MM, DD)

# Task
# 1.Write a Python program to find a person's age using the datetime module. Take the date of birth as input from the user.
from datetime import datetime
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
today = datetime.now()
age = today.year - birth_date.year
days = (today - birth_date).days
print("Your age is:", age)
print("You have lived for", days, "days")

# 2.Write a Python program to Take your birth date from the user and print the day of the week you were born?
from datetime import datetime
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
birth_day = birth_date.strftime("%A")
print("You were born on",birth_day)

# 3.Write a Python program to take a date from the user and print how many days are left until that date.
from datetime import datetime
future_date_input = input("Enter your today date (YYYY-MM-DD): ")
future_date = datetime.strptime(future_date_input, "%Y-%m-%d")
todays_date = datetime.now()
difference =  future_date - todays_date
print('the no. of days remaining is:', difference)

# 4.Write a Python program to take a date of birth from the user and print the person’s exact age in years and months.
from datetime import datetime
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
today = datetime.now()
years = today.year - birth_date.year
months = today.month - birth_date.month
if months < 0:
    years -= 1
    months += 12
print("Your age is:", years, "years and", months, "months")
