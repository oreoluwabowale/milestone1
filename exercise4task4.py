print( "Palindrome checker program")

word = input("Please enter a word: ")

word_palindrome = ""


for l in range(1, len(word) +1):
    word_palindrome += word [l * -1]

if word == word_palindrome or word == word_palindrome.capitalize() or word == word_palindrome.upper():
    print("word " + word_palindrome + " is a palindrome")
    
else:
     print("word " + word_palindrome + " is  not a palindrome")
    
