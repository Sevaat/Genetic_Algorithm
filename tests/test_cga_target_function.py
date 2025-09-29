def test_get_result_user_defined_function(cga_config, cga_population, cga_population_with_tf):
    # Тест на определение значения целевой функции для каждой особи популяции
    population = cga_config.settings.target_function(cga_population)
    for i in range(len(population)):
        assert population[i] == cga_population_with_tf[i]
        assert population[i].rank == cga_population_with_tf[i].rank
