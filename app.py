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
params.npop = 50
params.pc = 1
params.gamma = 0.1
params.mu = 0.01
params.sigma = 0.1

#Run GA
out = ga.run(problem, params)

#Results

#plt.plot(out.bestcost)
plt.semilogy(out.bestcost)
plt.xlim(0, params.maxit)
plt.xlabel("Iteration")
plt.ylabel("Best Cost")
plt.title("GA")
plt.grid(True)
plt.show()



