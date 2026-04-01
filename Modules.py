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
# The collections module is a Python module that gives special data structures (advanced versions of list, dict, tuple).

# Types of collections module:
# 1. Counter (Counting made easy)
# Used to count elements automatically
from collections import Counter
data = ['a', 'b', 'a', 'c', 'a']
print(Counter(data))
# Counting words, votes, product sales

# 2.defaultdict  (No key error)
# Normal dict gives error if key not found
# defaultdict gives default value
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(d)
# Use case: counting, grouping data

# 3.namedtuple (Tuple with names)
# Access values using names instead of index
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age'])
s = Student('Narendra', 28)
print(s.name)
# Easier to read than normal tuple

# 4.deque (Fast insert/remove)
# Fast add/remove from both ends
# Works like queue (FIFO) and stack
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
print(d)

# 5.OrderedDict (Keeps order)
# Stores items in insertion order
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