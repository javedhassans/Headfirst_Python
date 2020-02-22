""""This code checks for the time if the presenttime is odd or not odd
this code is taken from book Head_first_python by paul Barry"""


# creating the list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# asking for a word input from user
word = input("provide a word to search fo vowels")
# creating an empty list found
found = []
# program to check the new letters
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
