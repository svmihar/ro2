from numpy import sqrt
from scipy.optimize import minimize

def obj(x): 	
	return sqrt((x[0]-20)**2 + x[1]**2) + sqrt(x[0]**2 + (x[1]-20)**2)
def constraint(x): 
	return(x[0]**2 + x[1]**2 - 400**2)

const={
	'type': 'ineq', 
	'fun': constraint
}
x0 = (0,0)

solution = minimize(obj, x0, constraints=const)
print(solution['fun'])
print(solution['x'])


