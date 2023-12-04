import numpy as np
import math
def func(r,theta):
    r = r + .5*np.random.random_sample()
    ans = [2+r*math.cos(theta),2+r*math.sin(theta)]
    return ans

thetas = np.linspace(0, 2*math.pi, num=100)
gans = [func(1,theta) for theta in thetas]

garr = np.array(gans)
np.save('greenCirc.npy', garr)


rans = [func(2,theta) for theta in thetas]

rarr = np.array(rans)
np.save('redCirc.npy', rarr)

bans = [func(3,theta) for theta in thetas]

barr = np.array(bans)
np.save('blueCirc.npy', barr)


all_points =gans
all_points.extend(rans)
all_points.extend(bans)

def kerFunc(x,y):
    return (np.dot(x,y)+1)**2




kerMat = [ [kerFunc(x,y) for x in all_points] for y in all_points ]
oneNs = np.ones((300,300))*(1/300)

kerMat = kerMat - oneNs*kerMat - kerMat*oneNs + oneNs*kerMat*oneNs

np.save("kerMat.npy",kerMat)
print(len(garr))
kerMat = [garr,rarr,barr]
print(len(kerMat))
np.save("kerMatArrange.npy",kerMat)

