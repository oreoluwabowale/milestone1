print("Reverse sentence program".center(40))
print()
sentence = input("Please enter a sentence: ")
reverse_sentence = ""

for l in range(1, len(sentence) +1):
    reverse_sentence += sentence[l * -1]

print(reverse_sentence)

print("\"" + sentence + "\" reversed is \"" + reverse_sentence + "\"")
