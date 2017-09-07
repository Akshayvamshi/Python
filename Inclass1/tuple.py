mylist=["PHP","python","Java"]

#for i in range(len(mylist)):
 #   mylist[i]= (len(mylist[i]),mylist[i])

for i in mylist:
    print("ras",len(i))
    mylist[i] = (len(i), mylist[i])


print(mylist[:])

mylist.sort()
print(mylist[:])

print(mylist[len(mylist)-1])
