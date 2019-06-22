import math
import numpy as np

"""For the start of this problem we are going to assume"""
#side length of field

L = 30
tol = 20
"""
We are also going to be starting with the fence coming out of the bottom
left hand corner, bottom right hand corner, and middle top. These will be
connected in the middle to evenly divide the space
"""
#where our fences are tethered
N = [0,0]
S_t = 99999999999
for x in range(0,L+1):
    for y in range(0,L+1):
        #were gonna round the areas to integer values for now
        A_1 = round(x * y / 2 + x * (L - y) / 2)
        A_2 = round((L - x) * y / 2 + (L - x) * (L - y))
        A_3 = round(L * y / 2 )
        #if all areas are equal the program will calculate the fence length
        #print(A_1, A_2, A_3, x, y)
        if ((A_2 - tol) <= A_1 <= (A_2 + tol) and  (A_2 - tol) <= A_3 <= (A_2 + tol)) or ((A_1 - tol) <= A_2 <= (A_1 + tol) and  (A_1 - tol) <= A_3 <= (A_1 + tol)) or ((A_3 - tol) <= A_1 <= (A_3 + tol) and  (A_3 - tol) <= A_2 <= (A_3 + tol)):
            print('Theyre equal', A_1, A_2, A_3)
            S_1 = math.sqrt(x ** 2 + y ** 2)
            S_2 = math.sqrt((x - L / 2) ** 2 + (L - y) ** 2)
            S_3 = math.sqrt(y ** 2 + (L - x) ** 2)
            S_temp = S_1 + S_2 + S_3
            if S_temp < S_t:
                S_t = S_temp
                N[0] = x
                N[1] = y
print(N)
print(round(S_t))
""" 
Current Issue:
The main issue here is the constraints that are imposed by all 3 plots being 
equally sized.
Even with the tolerance that I have listed being +- 20 it still rarely gets 
a correct set
Future Improvements:
The points where the slices extend from the perimeter can't be fixed and should
be varied so a proper grid search can be done.
"""