import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import ga

#sphere test Function
def sphere(x):
    return sum(x**2)

#Problem defenition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

#GA Parameters
params = structure
params.maxit = 100
params.npop = 20

#Run GA
out = ga.run(problem, params)

#Results



