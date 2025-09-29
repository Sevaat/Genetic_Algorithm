def test_elite(cga_population_with_tf, cga_mutants, cga_replacement_elite):
    # Тест на отбор элитных особей
    from src.classical_genetic_algorithm.model.cga_replacement import Replacement
    population = Replacement.elite(cga_population_with_tf, cga_mutants)
    assert len(population) == 10
    for i in range(len(population)):
        assert population[i] == cga_replacement_elite[i]

def test_simple_cut(cga_population_with_tf, cga_mutants, cga_replacement_simple_cut):
    # Тест на отбор простым срезом
    from src.classical_genetic_algorithm.model.cga_replacement import Replacement
    population = Replacement.simple_cut(cga_population_with_tf, cga_mutants)
    assert len(population) == 10
    for i in range(len(population)):
        assert population[i] == cga_replacement_simple_cut[i]