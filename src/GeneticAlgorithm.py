import src.utils.GlobalVariables as GV


def genetic_algorithm():
    population = GV.GENETIC_ALGORITHM.population_initialization()
    population = GV.GENETIC_ALGORITHM.target_function(population)

    era = 0
    while era < GV.PARAMETERS.number_of_eras:
        parents = GV.GENETIC_ALGORITHM.parent_selection(population)
        childrens = GV.GENETIC_ALGORITHM.recombination(parents)
        del parents
        mutants = GV.GENETIC_ALGORITHM.mutation(childrens)
        del childrens
        mutants = GV.GENETIC_ALGORITHM.target_function(mutants)
        population = GV.GENETIC_ALGORITHM.replacement(population, mutants)
        del mutants
        if GV.GENETIC_ALGORITHM.stops(population):
            break
        else:
            era += 1
    return population[:GV.PARAMETERS.number_of_results]



if __name__ == '__main__':
    pass
