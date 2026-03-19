with open("sample.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a test file.\n")

# append
with open("sample.txt", "a") as f:
    f.write("New line added.\n")

print("File created and updated.")