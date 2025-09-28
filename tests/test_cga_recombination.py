def test_get_points(cga_config):
    # Тест, что точка разделения попадет в диапазон между первым и последним элементами
    from src.classical_genetic_algorithm.model.cga_recombination import Recombination
    import random
    random.seed(1)
    for _ in range(100):
        points = Recombination.get_points(6)
        assert points[0] == 0
        assert points[2] == 6
        assert 0 < points[1] < 6

def test_point_crossing(cga_population_with_tf, cga_parents, cga_children):
    # Тест на создание детей точечной рекомбинацией
    from src.classical_genetic_algorithm.model.cga_recombination import Recombination
    import random
    random.seed(1)
    children = Recombination.point_crossing(cga_population_with_tf, cga_parents)
    for i in range(len(children)):
        assert children[i] == cga_children[i]

def test_segmental_crossing(cga_population_with_tf, cga_parents):
    # Тест на создание детей рекомбинацией сегментами
    from src.classical_genetic_algorithm.model.cga_recombination import Recombination
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    import random
    random.seed(1)
    children = Recombination.segmental_crossing(cga_population_with_tf, cga_parents)
    assert children[0] == Individual().new_individual_by_code('000101')
    assert len(children) == 2

def test_even_crossing(cga_population_with_tf, cga_parents):
    # Тест на создание детей равномерным скрещиванием
    from src.classical_genetic_algorithm.model.cga_recombination import Recombination
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    import random
    random.seed(1)
    children = Recombination.even_crossing(cga_population_with_tf, cga_parents)
    assert children[0] == Individual().new_individual_by_code('010101')
    assert len(children) == 2
