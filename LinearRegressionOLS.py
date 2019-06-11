import numpy as np 
"""For the purposes of developing this from the ground up we are going to be
   building this assuming that we are inputting the values 
   directly into the file"""
"""Here we are being fed the dimensions of the array where 'n' is the number of
   features and 'm' is the number of data points"""
print("Please input first number of features and then number of rows of data")
m,n = [int(i) for i in input().strip().split(' ')]
"""Here we are creating two empty lists to store our variables"""
X = []
Y = []
"""We are then continuing to take the input that will then fill the array,
   formatting the input data is as follows
   X11   X21  Y1
   X12   X22  Y2"""
for i in range(n):
    print("Please input row {}".format(i))
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])
print(m,n)
print(X)
print(Y)