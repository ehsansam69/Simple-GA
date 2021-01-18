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
    gamma = params.gamma
    mu = params.mu
    sigma = params.sigma

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

    # Main Loop, cross over and mutation and have a population of offsprings

    for it in range(maxit):

        popc =[]
        for k in range(nc//2):
            #select parents randomly
            q = np.random.permutation(npop)
            p1 = pop[q[0]]
            p2 = pop[q[1]]

            #perform cross over
            c1, c2 = crossover(p1,p2,gamma)

            #perform mutation
            c1 = mutate(c1, mu, sigma)
            c2 = mutate(c2, mu, sigma)





    # Output
    out = structure()
    out.pop = pop
    return out

#cross over func
def crossover(p1,p2,gamma =0.1):
    c1 = p1.deepcopy()
    c2 = p2.deepcopy()
    alpha = np.random.uniform(-gamma,1+gamma,*c1.position.shape)
    c1.position = alpha*p1.position +(1-alpha)*p2.position
    c2.position = alpha*p2.position +(1-alpha)*p1.position
    return c1,c2

def mutate(x, mu, sigma):
    y = x.deepcopy()
    flag = np.random.rand(*x.position.shape) <= mu   #an array of trues and falses
    ind = np.argwhere(flag) # where flag is true
    y.position[ind] += sigma*np.random.randn(*ind.shape)  #randn normaly distrubuted number 0 to 1 with sigma
    return y






