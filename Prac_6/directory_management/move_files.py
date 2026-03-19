import shutil
import os

# ensure directory exists
os.makedirs("destination", exist_ok=True)

# move file
if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "destination/sample.txt")
    print("File moved.")

# copy back
shutil.copy("destination/sample.txt", "sample_copy.txt")
print("File copied.")