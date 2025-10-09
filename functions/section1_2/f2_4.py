"""
Temperature Tracker
"""

temps = []

def add_temp(grade: float, scale: str):
    global temps
    temps.append([grade, scale])

add_temp(40, "C")
add_temp(87, "F")
add_temp(215, "K")

print(temps)