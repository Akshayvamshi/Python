#Taking the input string from terminal and storing it.
str = input("enter the string")
#converting string to lower case
#splitting string into words and storing the sorted elements (duplication will be removed)
str1 = sorted(set((str.lower().split())))
#joining the unique sorted words
str2 = " ".join(str1)
print(str2)
