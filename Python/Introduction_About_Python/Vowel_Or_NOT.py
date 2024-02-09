def is_vowel(letter):
    vowels = ['a' , 'e', 'i', 'o', 'u']
    
    if letter.lower() in vowels:
        return True
    else:
        return False
    
input_letter = input("Enter a letter: ")

if len(input_letter) == 1 and input_letter.isalpha():
    if is_vowel(input_letter):
        print(input_letter, "is a Vowel.")
    else:
        print(input_letter, "is not a Vowel.")
else:
    print("Invaild input please enter a single letter.")