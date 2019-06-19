import math
import numpy as np 


def sigmoid(func):
    sig = math.e ** func / (math.e ** func + 1)
    return sig

def make_layer(arr, size):
    layer = np.random.rand(arr.size,size)
    return layer

inflow = np.random.rand(20)
first = make_layer(inflow, 5)
out_from_first = sigmoid(inflow@first)
second = make_layer(out_from_first,5)
out_from_second = sigmoid(out_from_first@second)
final = make_layer(out_from_second,1)
output = sigmoid(out_from_second@final)
print(output)


