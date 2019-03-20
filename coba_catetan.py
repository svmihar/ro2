import numpy as np
from scipy.optimize import minimize

def objective(x):
    return 2*x[0]**2 + x[1]**2 + 4*x[2]**2

def constraint1(x):
    return x[0]+2*x[1]-x[2]-6

def constraint2(x):
    return 2*x[0] - 2*x[1] + 3*x[2] - 12

# initial guesses
x0 = np.zeros(3)
print('Initial Objective: ' + str(objective(x0)))

con1 = {'type': 'eq', 'fun': constraint1} 
con2 = {'type': 'eq', 'fun': constraint2}
cons = ([con1,con2])
solution = minimize(objective,x0,method='SLSQP',constraints=cons)
x = solution.x

# show final objective
print('Final Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
