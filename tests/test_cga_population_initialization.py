def test_get_new_random_population(cga_population):
    # Тест на создание популяции
    from src.classical_genetic_algorithm.model.cga_population_initialization import Population
    import random
    random.seed(1)
    population = Population.get_new_random_population()
    for i in range(len(population)):
        assert population[i] == cga_population[i]