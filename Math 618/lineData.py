import codecs,json
import numpy as np

def func(x):
    ans = .5*x + np.random.random_sample()
    return ans

xs = np.linspace(-4,4, num=100)
ys = [func(x) for x in xs]

arr = np.array([xs,ys])
np.save('lineData.npy', arr)


A = [1,2]

X = [  [x*y for x in A] for y in A ]
print(X)

np.savetxt('lineData.txt', arr)