def test_elite(cga_population_with_tf, cga_mutants):
    from src.classical_genetic_algorithm.model.cga_replacement import Replacement
    population = Replacement.elite(cga_population_with_tf, cga_mutants)
    assert len(population) == 10