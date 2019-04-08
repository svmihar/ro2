from pyomo.environ import * 
from pyomo.opt import SolverFactory

opt = SolverFactory('glpk')

model = ConcreteModel() #concrete karena variabel sudah jelas 

model.x1 = Var(wihin = NonNegativeIntegers)
model.x2 = Var(wihin = NonNegativeIntegers)

#deviational
model.n1 = Var(wihin = NonNegativeIntegers)
model.p1 = Var(wihin = NonNegativeIntegers)
model.n2 = Var(wihin = NonNegativeIntegers)
model.p2 = Var(wihin = NonNegativeIntegers)
model.n3 = Var(wihin = NonNegativeIntegers)
model.p3 = Var(wihin = NonNegativeIntegers)
model.n4 = Var(wihin = NonNegativeIntegers)
model.p4 = Var(wihin = NonNegativeIntegers)

#  define objective funciton 
model.obj = Objective(expr = model.p1 + model.p2 + model.n3 + model.p4)

# define constraint
model.con1 = Constraint(expr = 2* model.x1 + 4*model.x2 + model.n1 - model.p1 == 600)
model.con2 = Constraint(expr = 5 * model.x1 + 3 * model.x2 + )
