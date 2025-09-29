def test_mutation(cga_population_with_tf, cga_children):
    # Тест на создание мутантов
    from src.classical_genetic_algorithm.model.cga_mutation import Mutation
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    import random
    random.seed(1)
    mutants = Mutation.mutation(cga_population_with_tf, cga_children)
    assert mutants[0] == Individual().new_individual_by_code('000001')
    assert len(mutants) == 7