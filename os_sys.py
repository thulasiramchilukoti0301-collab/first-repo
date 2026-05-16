import os
import sys

print("Current Directory:", os.getcwd())

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()
    print(f"Usage: {sys.argv[0]} <directory_path>")

files = os.listdir(path)

for file in files:
    ext = os.path.splitext(file)[1]
    if ext in ['.txt', '.csv']:
        full_path = os.path.join(path, file)

        size = os.path.getsize(full_path)
        print(f"{file} - {size} bytes")