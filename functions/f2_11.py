def outer():
    print("Outer start")
    
    def inner():
        print("Inner call")
        
        def third():
            print("Third")
        third()
    inner()
outer()