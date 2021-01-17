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
    pc = params.pc
    nc = np.round(pc*npop/2)*2

    # empty individual template

    empty_individual = structure()
    empty_individual.position = None
    empty_individual.cost = None

    # Best solution

    bestsol = empty_individual.deepcopy()   # have no effect in other when changed
    bestsol.cost = np.inf

    # Initialize population
    pop = empty_individual.repeat(npop)
    for i in range(0, npop):
        pop[i].position = np.random.uniform(varmin,varmax, nvar)
        pop[i].cost = costfunc(pop[i].position)
        if pop[i].cost < bestsol:  # the better solution is the one with less cost
            bestsol = pop[i].deepcopy()

    # Best cost of itteration
    bestcost = np.empty(maxit)

    # Main Loop, crross over and mutation and have a population of offsprings

    for it in range(maxit):

        popc =[]
        for k in range(nc//2):





    # Output
    out = structure()
    out.pop = pop
    return out