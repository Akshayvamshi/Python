import numpy as np
#creating vector of size 15 with some random values between 1-15
myvector = np.random.randint(1,15, size=15)
print(myvector)
x=myvector.max()
#printing the max value in the vector
print("Max value in the vector is:",x)
print("Replacing max value with 100")
# Replacing the max value in the vector with 100
for i in range(0,14):
    if(myvector[i]==x):
        myvector[i]=100
print(myvector)