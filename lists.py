thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# len function can be used to return the number of items in a list
print(len(thislist))

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]



# From Python's perspective, lists are defined as objects with the data type 'list':
print(type(list1))



#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

