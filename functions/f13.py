def count_vowels(word: str) -> bool:
    vowels = "aeiou"
    
    for c in vowels:
        if c in vowels:
            return True
    
    return False


word = "wwww"


a, b = map(int, input("Enter two numbers: ").split())