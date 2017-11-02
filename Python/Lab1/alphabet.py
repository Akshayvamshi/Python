import string
input_string=input('Enter the string')
f= set(input_string.lower())  #input string is converted to set of individual lowercase characters
print(f)
alphabet=set(string.ascii_lowercase) #letters of alphabets are stored in set
if f >= alphabet: #input string is compared with the set of letters of alphabets
    print('given string has all letters of alphabet')
else:
    print("string doesn't contains all letters of alphabet")
