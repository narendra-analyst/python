# For else:
# Is execute after the for loop complete its iteration over the entire sequence,but only if a break statement didn't terminate the loop.
numbers = [1,2,3,4,5]
target = 6
for num in numbers :
  if num == target :
    print(f"found {target}")
    break
else :
  print(f"{target} not found")

# While else:
# The else block wiht a while loop executes only if the loop terminates normally, meaning the loop condition become false.
i = 1
while i < 6 :
  print(i)
  i += 1
else :
  print("Loop completed normally, i is now 6")
