from ypstruct import structure
import numpy as np

def run(problem, params):

    #Problem Information
    costfunc = problem.costfunc
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax

    #Parameters
    maxit = params.maxit
    npop = params.npop

    # empty individual template

    empty_individual = structure()
    empty_individual.position = None
    empty_individual.cost = None

    # Initialize population
    pop = empty_individual.repeat(npop)
    for i in range(0, npop):
        pop[i].position = np.random.uniform(varmin,varmax, nvar)
        pop[i].cost = costfunc(pop[i].position)

    # Output
    out = structure()
    out.pop = pop
    return out