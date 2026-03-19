"""import shutil

# Copy file (backup)
shutil.copy("sample.txt", "sample_backup.txt")

print("File copied to sample_backup.txt")"""

"""import os

# Safe delete function
def safe_delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully.")
    else:
        print(f"{filename} does not exist.")

# Example usage
safe_delete("sample_backup.txt")"""