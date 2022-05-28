# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = (input("Enter your first word: ").replace(" ", "")) #The replace function removes every space in the words or phrases
    anagram = (input("Enter your second word: ").replace(" ", "")) #The lower function was added to process input with capital letters
    return sorted(word.lower()) == sorted(anagram.lower()) #If the words are anagrams, it will return true if not false

print(find_anagram("word", "anagram"))