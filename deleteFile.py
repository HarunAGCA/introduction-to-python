import os

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# Note: You can only remove empty folders.
if(os.path.exists("myfolder")):
    if(os.path.isdir("myfolder")):
        os.rmdir("myfolder")
    else:
        print("'myfolder' is not a directory")
else:
    print("'myfolder' does not exist")