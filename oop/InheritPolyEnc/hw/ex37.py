class One:
    def run(self):
        print("One is running")
        

class Two:
    def run(self):
        print("Two is running")
        

class Three:
    def walk(self):
        print("Walking...")
        

def start(obj: One | Two):
    obj.run()


one1 = One()
two1 = Two()
three1 = Three()

start(one1)
start(two1)
start(three1)