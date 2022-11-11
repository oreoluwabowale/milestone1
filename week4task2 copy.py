print("Star Wars name generator".center(40))

print()
firstName = input("Please enter your first name:")
lastName = input("Please enter your last name:")
mothersMaidenName = input("Please enter your Mother's maiden name:")
nameOfCity= input("Please enter the name of the city you were born in:")

starWarsName = firstName[:3] + lastName[:3].lower()+ " " + mothersMaidenName[:2] + nameOfCity[:3].lower()
print(starWarsName) 