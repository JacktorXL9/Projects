import numpy as np
from numpy.linalg import inv 
"""For the purposes of developing this from the ground up we are going to be
   building this assuming that we are inputting the values 
   directly into the file"""
"""Here we are being fed the dimensions of the array where 'm' is the number of
   features and 'n' is the number of data points"""
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
    print("Please input row {}".format(i+1))
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])
X = np.array(X,float)
Y = np.array(Y,float)
X = np.c_[ np.ones(n), X]
Beta = np.dot(np.dot(inv(np.dot(np.transpose(X), X)), np.transpose(X)), Y)
print('Please input your {} data points'.format(m))
X_input = []
data = input().strip().split(' ')
X_input.append(data)
X_input = np.array(X_input,float)
X_input = np.c_[ np.ones(1), X_input]
Y_new = np.dot(X_input, Beta)


print(Y_new)
