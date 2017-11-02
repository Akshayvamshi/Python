#This code generates dictionary of squares of integers(>=1)
a = int(input("Enter an integer upto which you want to generate the dictinary of squares"))
#Function dict() to generate dictionary of squares from 1 to given number
#If any wrong input is given (i.e <1) then it asks again until valid input is given
def dict(a):
    if (a>=1):
        dictionry = {x: x * x for x in range(1, a + 1)}
        print(dictionry)
    else:
        print("Given input is not valid")
        a = int(input("Enter valid number"))
        dict(a) #Recursion - calling the function again until valid input is given
dict(a)

