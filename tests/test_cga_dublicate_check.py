def test_individual_addition(cga_config):
    # Тест на проверку повторений в популяции
    from src.classical_genetic_algorithm.model.cga_individual import IndividualFactory
    from src.classical_genetic_algorithm.utils.cga_duplicate_check import DuplicateCheck
    import random
    random.seed(1)
    individual1 = IndividualFactory.new_random_individual()
    individual2 = IndividualFactory.new_random_individual()
    individual3 = IndividualFactory.new_random_individual()
    individual4 = IndividualFactory.new_random_individual()
    population = [individual1, individual2, individual3]
    assert DuplicateCheck.individual_addition(population, individual4)
    assert not DuplicateCheck.individual_addition(population, individual1)