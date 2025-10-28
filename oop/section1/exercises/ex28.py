class TempFile:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"File<name={self.name}>"
    
    def __del__(self):
        print("File deleted successfully.")
        del self
        
f1 = TempFile("hello.txt")

print(f1)

del f1