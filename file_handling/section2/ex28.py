import os
import time


os.makedirs("testdir")
os.chdir("./testdir")
for i in range(5):
    open(f"file_{i+1}.txt", "x")

open("file6.go", "x")

print("TXT files are created...")
time.sleep(10)

for filepath in os.listdir(os.curdir):
    filename, ext = filepath.split(".")
    if ext == "txt":
        os.rename(f"{filename}.{ext}", f"{filename}.bak")
        
print("Waiting for user to check...")
time.sleep(60)

for file in os.listdir(os.curdir):
    os.remove(file)

os.chdir(os.pardir)
os.rmdir("./testdir")

print("Musorlar tozalandi!")