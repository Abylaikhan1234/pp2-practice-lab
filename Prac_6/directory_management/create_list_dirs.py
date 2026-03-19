"""import os

# Create nested directories
os.makedirs("parent_dir/child_dir/grandchild_dir", exist_ok=True)

print("Nested directories created.")"""

"""import os

path = "parent_dir"

# List all files and directories
items = os.listdir(path)

print("Contents of directory:")
for item in items:
    print(item)"""

"""import os

search_path = "."
extension = ".txt"

print(f"Files with '{extension}' extension:")

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))"""