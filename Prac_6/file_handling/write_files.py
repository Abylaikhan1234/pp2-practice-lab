# Create and write to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This is the second line.\n")

print("File created and data written.")

# Append new lines
"""with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("Another appended line.\n")

# Verify updated content
with open("sample.txt", "r") as file:
    updated_content = file.read()

print("Updated file contents:")
print(updated_content)"""