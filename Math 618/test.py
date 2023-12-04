import numpy as np

arr_loaded = np.load('lineData.npy')
print(arr_loaded)


A = [1,2]

X = [  [x*y for x in A] for y in A ]
print(X)

circ_load = np.load('greenCirc.npy')
print(circ_load)