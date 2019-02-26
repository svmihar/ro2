import numpy as np 
import matplotlib.pyplot as plt 

#plot circle
x = 8*np.ones(8)
y = 8*np.ones(8)
r = np.arange(8)/np.sqrt(2)

phi = np.linspace(0.0,2*np.pi,100)
na = np.newaxis

#first axis of array varies the angle 
#second varies the circle

x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])
ax = plt.plot(x_line,y_line,'-')

#plot line
x1 = np.linspace(0,10,1000)
x2 = 12*np.ones(1000)-x1

bx = plt.plot(x1,x2,label='$x_1+x_2-12<=0$')
d= np.zeros(len(x2))
plt.fill_between(x1,x2, where=x2>=d,color='grey')
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$y_1$')
plt.show()