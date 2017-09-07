str=input("enter numbers and letters")
leng=len(str)
dig=0
alpha=0
for i in range(leng):
    if str[i].isdigit():
        dig=dig+1
    elif str[i].isalpha():
        alpha=alpha+1

print("%d digits and %d alphabets" %(dig,alpha))
