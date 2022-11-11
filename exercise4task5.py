print("Python variable name checker")
print(" -" * 14)
print()
variable_name = input("Input the name of the variable: ")

if variable_name[0].isnumeric():
    print("variable name, ", variable_name, "is not valid for python")
    
#else:
 #       print("variable name,", variable_name, "is valid for python")
        
#elif variable_name[0].upper and variable_name[0]!="_":
 #   print("variable name,", variable_name, "is valid but not for python")
#
elif not variable_name.replace("_", "").isalnum():
    print("variable name, ", variable_name, "is not valid because it contains characters other than a to z, A to Z, 0 to 9 or underscore")
 
else:
    print("variable name, ", variable_name, "is valid for python")