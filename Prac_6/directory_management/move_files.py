import shutil

# Copy file
shutil.copy("sample.txt", "parent_dir/sample_copy.txt")
print("File copied.")

# Move file
shutil.move("parent_dir/sample_copy.txt", "parent_dir/child_dir/sample_moved.txt")
print("File moved.")