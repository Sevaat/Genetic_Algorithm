def test_sort_by_more(cga_population_with_tf):
    # Тест на проверку корректной сортировки по возрастанию
    from src.classical_genetic_algorithm.utils.cga_purpose import Purpose
    individuals = Purpose.sort_by_more(cga_population_with_tf)
    assert individuals[0].rank == 13
    assert individuals[-1].rank == 16
    for i in range(len(individuals)-1):
        assert individuals[i].rank <= individuals[i+1].rank

def test_sort_by_less(cga_population_with_tf):
    # Тест на проверку корректной сортировки по убыванию
    from src.classical_genetic_algorithm.utils.cga_purpose import Purpose
    individuals = Purpose.sort_by_less(cga_population_with_tf)
    assert individuals[0].rank == 16
    assert individuals[-1].rank == 13
    for i in range(len(individuals)-1):
        assert individuals[i].rank >= individuals[i+1].rank