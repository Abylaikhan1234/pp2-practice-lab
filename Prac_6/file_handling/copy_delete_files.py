import shutil
import os

# copy file
shutil.copy("sample.txt", "backup_sample.txt")
print("File copied.")

# safe delete
if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
    print("Backup deleted.")
else:
    print("File not found.")