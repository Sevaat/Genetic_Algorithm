from unittest.mock import patch


def test_get_weights(cga_population_with_tf):
    # Тест на оценку весов для каждой особи
    from src.classical_genetic_algorithm.model.cga_parent_selection import Selection
    weights = Selection.get_weights(cga_population_with_tf)
    for w in weights:
        print(w)
    assert abs(weights[0] - 0.9041) < 0.0001
    assert abs(weights[1] - 0.9041) < 0.0001
    assert abs(weights[2] - 0.8904) < 0.0001
    assert abs(weights[3] - 0.911) < 0.0001
    assert abs(weights[4] - 0.8973) < 0.0001
    assert abs(weights[5] - 0.8904) < 0.0001
    assert abs(weights[6] - 0.8904) < 0.0001
    assert abs(weights[7] - 0.911) < 0.0001
    assert abs(weights[8] - 0.9041) < 0.0001
    assert abs(weights[9] - 0.8973) < 0.0001

def test_standard_selection(cga_population_with_tf):
    from src.classical_genetic_algorithm.model.cga_parent_selection import Selection
    import random
    random.seed(1)

    # Тест, что родители разные
    parents = Selection.standard_selection(cga_population_with_tf)
    for p1, p2 in parents:
        assert p1 != p2

def test_stochastic_universal_sampling(cga_population_with_tf):
    from src.classical_genetic_algorithm.model.cga_parent_selection import Selection
    import random
    random.seed(1)

    # Тест, что родители разные
    parents = Selection.stochastic_universal_sampling(cga_population_with_tf)
    for p1, p2 in parents:
        assert p1 != p2

