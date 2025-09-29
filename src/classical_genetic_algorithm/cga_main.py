def start():
    """
    Функция для оптимизации с использованием классического генетического алгоритма
    :return:
    """
    from src.classical_genetic_algorithm.options_ga.cga_config import Config
    config = Config()
    population = config.settings.population_initialization()
    population = config.settings.target_function(population)
    era = 0
    while era < config.parameters.number_of_eras:
        parents = config.settings.parent_selection(population)
        children = config.settings.recombination(population, parents)
        del parents
        mutants = config.settings.mutation(population, children)
        del children
        mutants = config.settings.target_function(mutants)
        population = config.settings.replacement(population, mutants)




    #     del mutants
    #     if GV.GENETIC_ALGORITHM.stops(population):
    #         break
    #     else:
    #         era += 1
    # return population[:GV.PARAMETERS.number_of_results]
