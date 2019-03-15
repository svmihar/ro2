import numpy as np 
import time
pi = 0
accuracy = 1000
t0 = time.time()
for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))

    print(pi)

result = round(time.time()-t0)
print('finished in ', result,'seconds')



from random import random 
from math import sqrt, pi 
from multiprocessing import Pool 
import multiprocessing, logging
mpl = multiprocessing.log_to_stderr()
mpl.setLevel(logging.INFO)

def estimate_pi(n): 
    i, inside = 0,0
    while i < n: 
        x,y = random(), random()
        if np.sqrt(x**2 + y**2) <=1:
            inside += 1
        i+=1
    ratio = 4.0*inside/n
    return ratio

if __name__ == '__main__': 
    with Pool(4) as p: 
        pis = p.map(estimate_pi, [40000000]*4)
        print(pis)
        mypi = sum(pis)/4
        error = mypi - np.pi
        print(f"My pi: {mypi}, error = {error}")
        cpname = multiprocessing.current_process().name
# print cpname
        mylogger.info("{0} is currently doing...".format(cpname))