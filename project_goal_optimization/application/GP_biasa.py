from pyomo.environ import * 
from pyomo.opt import SolverFactory

opt = SolverFactory('cbc')
f1 = 4977523000
f2 = 2053334000

model = ConcreteModel() #concrete karena variabel sudah jelas 

model.x1 = Var(within = NonNegativeIntegers)
model.x2 = Var(within = NonNegativeIntegers)
model.x3 = Var(within = NonNegativeIntegers)
model.x4 = Var(within = NonNegativeIntegers)

#deviational
model.d11 = Var(within = NonNegativeIntegers)
model.d12 = Var(within = NonNegativeIntegers)
model.d21 = Var(within = NonNegativeIntegers)
model.d22 = Var(within = NonNegativeIntegers)
model.d31 = Var(within = NonNegativeIntegers)
model.d32 = Var(within = NonNegativeIntegers)
model.d41 = Var(within = NonNegativeIntegers)
model.d42 = Var(within = NonNegativeIntegers)
model.d51 = Var(within = NonNegativeIntegers)
model.d52 = Var(within = NonNegativeIntegers)
model.d61 = Var(within = NonNegativeIntegers)
model.d62 = Var(within = NonNegativeIntegers)
model.d71 = Var(within = NonNegativeIntegers)
model.d72 = Var(within = NonNegativeIntegers)


# define constraint
model.con1 = Constraint(expr = model.x1 + model.d11 - model.d12 == 41890.87)
model.con2 = Constraint(expr = model.x2 + model.d21 - model.d22 == 33379.18)
model.con3 = Constraint(expr = model.x3 + model.d31 - model.d32 == 31558.86)
model.con4 = Constraint(expr = model.x4 + model.d41 - model.d42 == 34756.75)
model.con5 = Constraint(expr = 12450*model.x1 + 10800*model.x2 + 15200*model.x3 + 7400*model.x4 + model.d51 >= f1) 
model.con6 = Constraint(expr = 5590*model.x1 + 4481*model.x2 + 7245*model.x3 + 1365*model.x4 + model.d61 >= f2)
model.con7 = Constraint(expr = 7.452*model.x1 + 8.273*model.x2 + 4.5206*model.x4 + model.d71 - model.d72 == 3444480)
model.con8 = Constraint(expr = model.d72 <= 1347840)
model.con9 = Constraint(expr = model.x1 >=0)
model.con10 = Constraint(expr = model.x2 >=0)
model.con11 = Constraint(expr = model.x3 >=0)
model.con12 = Constraint(expr = model.x4 >=0)
model.con13 = Constraint(expr = model.d11 >=0)
model.con14 = Constraint(expr = model.d21 >=0)
model.con15 = Constraint(expr = model.d31 >=0)
model.con16 = Constraint(expr = model.d41 >=0)
model.con17 = Constraint(expr = model.d12 >=0)
model.con18 = Constraint(expr = model.d22 >=0)
model.con19 = Constraint(expr = model.d32 >=0)
model.con20 = Constraint(expr = model.d42 >=0)
model.con21 = Constraint(expr = model.d51 >=0)

#  define objective funciton 
model.obj = Objective(expr = model.d11 + model.d12 + model.d21 + model.d22 +model.d31 + model.d32 + model.d41 + model.d42 + model.d51 + model.d61 + model.d71+model.d72)

opt.solve(model).write()
print(model.d11.value)
print(model.d12.value)
print(model.d21.value)



""""""

