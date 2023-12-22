import numpy as np
from lazy import *

N = 8096
print("step 1")
def createMatrix(n):
    return np.random.randn(n,n)

def mm(a, b):
    return force(a) @ force(b)

print("step 2")
m1 = lazy(createMatrix(N))
print("step 3")
m2 = lazy(createMatrix(N))
print("step 4")
print("step 5")
print("step 6")
print("step 7")
print("step 8")

c = lazy(mm, m1, m2)
print("step 9")
print("step 10")
print("step 11")
print("step 12")
print("step 13")

print(c)
