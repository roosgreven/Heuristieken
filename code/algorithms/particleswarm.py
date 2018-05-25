def particleSwarm(population, iterations):
    """ Particle swarm function that will increase the value of the given plan by
        step by step moving each house in the direction of the best known 
        floorplan. 

        Args: 
            population: a list of floorplans with the correct number of houses. 
            iterations: the number of times the population is updated during
        the algorithm. """
    
    # The population is updated in each iteration
    for i in range(iterations):
            
        population.updatePopulation()
                
    return population      