from scipy.spatial import distance
from math import sqrt
#Y = cdist(XA, XB, 'euclidean')
a = (0,20)
b = (20,0)
distance1 = []
distance2 = []

def euc(x,y): 
    euclidean_distance = sqrt( (x[0]-y[0])**2 + (x[1]-y[1])**2 )
    return euclidean_distance 

for i in range(400): 
    for j in range(400): 
        x = (i,j)
        print(x)
        distance1.append(euc(x,a))
        distance2.append(euc(x,b))
        

print(max(distance1), max(distance2))