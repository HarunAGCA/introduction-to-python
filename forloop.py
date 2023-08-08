fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# The range() function returns a sequence of numbers, starting
# from 0 by default, and increments by 1 (by default), and ends 
# at a specified number.
for x in range(2,6):
    print(x)


# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  print(x)
else:
  print("Finally finished!")