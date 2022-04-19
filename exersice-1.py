# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 

letter = input('Enter a letter from "a-z:')

# 2. Write the code that determines whether the letter entered is a vowel
if letter == 'a':
    print('You entered a vowel')
elif letter == 'e':
    print('You entered a vowel')
elif letter == 'i':
    print('You entered a vowel')
elif letter == 'o':
    print('You entered a vowel') 
elif letter == 'u':
    print('You entered a vowel')    
else:
    print('not a vowel')    

# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
letter = 'A'

print(f'The letter "{letter}" is a vowel')

second_letter = 'B'

print(f'The letter "{second_letter}" is a constant')

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':