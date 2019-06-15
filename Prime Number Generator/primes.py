import math
#f= open("primes.txt","w+")
x = int(input())
def generatelist(x):
    lst = []
    for i in range(2,x+1):
        lst.append(i)
    return lst
list = generatelist(x)
def Sieve_of_Eratosthenes(x):
    arr = generatelist(x)
    stop = int(math.sqrt(len(arr)+1))
    i = 0
    j = 0
    while i<=stop:
        n = arr[i]
        for j in range(2,int(x/n)+1):
            if j*n in arr:
                z = arr.index(j*n)
                arr.pop(z)
        i+=1
    return arr
print(Sieve_of_Eratosthenes(x))
