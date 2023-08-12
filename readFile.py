# Read whole file content
f = open("demofile.txt", "r")
print(f.read())

print('----------------')

# Read first 5 characters
f = open("demofile.txt", "r")
print(f.read(5))

print('----------------')

# Read line by line
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print('----------------')

# Read all content of file line by line
f = open("demofile.txt", "r")
for x in f:
  print(x)

print('----------------')

f = open("demofile.txt", "r")
print(f.readline())
f.close()