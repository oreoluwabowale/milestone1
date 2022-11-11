print(" Analysis of text".center(30))
print("-"*30)
userText= input("Please enter your text: ")

consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z", "W" , "Y"]
punctuation = [".", "?", ",", "'",";", ":", '"', "!", "-", "_", "[", "]", "{", "}", "...."]

def vowel(text):
    numberOfVowels = 0
    for i in range(len(text)):
        if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
            numberOfVowels +=1
    print("Number of vowels = ", numberOfVowels)

    



def letterConsonants(text):
    numberOfConsonants = 0
    for i in range(len(text)):
        for t in range(len(consonants)):
            if text[i] == consonants[t] or text[i] == consonants[t].lower():
                numberOfConsonants +=1
    print("Number of consonants = ", numberOfConsonants)
    
def digits(text):
    numberOfDigits = 0
    for i in range(len(text)):
        if text[i] == "1" or text[i] == "2" or text[i] == "3" or text[i] == "4" or text[i] == "5" or text[i] == "6" or text[i] == "7" or text[i] == "8" or text[i] == "9" or text[i] == "0":
            numberOfDigits +=1
    print("Number of Digits = ",numberOfDigits)
    
def allPunctuations(text):
    numberOfPunctuation = 0
    for i in range(len(text)):
        for t in range(len(punctuation)):
            if text[i] == punctuation[t]:
                numberOfPunctuation +=1
    print("Number of punctuation = ", numberOfPunctuation)
    
def whiteSpace(text):
    numberOfWhiteSpace = 0
    for i in range(len(text)):
        if text[i] == " " or text[i] == "   ":
            numberOfWhiteSpace +=1
    print("Number of white space = ", numberOfWhiteSpace)


vowel(userText)
letterConsonants(userText)
digits(userText)
allPunctuations(userText)
whiteSpace(userText)