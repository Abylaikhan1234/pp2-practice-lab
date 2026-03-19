import os

# create nested directories
os.makedirs("test_dir/sub_dir", exist_ok=True)

# list files and folders
for item in os.listdir("test_dir"):
    print(item)

# find .txt files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print("Found:", file)