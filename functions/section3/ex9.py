def moving_up():
    print("Moving up...")
    
def moving_down():
    print("Moving down...")


command_map = {
    "up": moving_up,
    "down": moving_down,
}

command_map["up"]()
command_map["down"]()