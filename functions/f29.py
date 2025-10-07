def custom_greet(name, **options):
    greet_string = f"Hello {name}"
    
    if "prefix" in options:
        greet_string = greet_string[:6] + options["prefix"] + " " + greet_string[6:]
    if "suffix" in options:
        greet_string += options["suffix"]
    
    return greet_string

print(custom_greet("Eshmat", prefix="dear", suffix="!!!"))