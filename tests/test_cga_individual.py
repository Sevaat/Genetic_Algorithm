def test_init(cga_config):
    # Тест на успешную инициализацию
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    individual = Individual()
    assert individual.code is None
    assert individual.rank is None

    individual = Individual().new_individual_by_code('001100')
    assert individual.code == '001100'
    assert individual.rank is None

    individual = Individual().new_individual_by_code('001000')
    assert individual is None

def test_str_and_transcript_individual(cga_config):
    # Тест на вывод данных особи в строку и перевода кода в генотип
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    individual = Individual()
    individual.code = '001100'
    individual.rank = 0
    assert str(individual) == f"Код: 001100. Значение ЦФ: 0. Генотип: ['1', '6', '7']"

def test_overstepping(cga_config):
    # Тест на проверку контроля выхода параметров особи за границы
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    individual = Individual()
    individual.code = '000000' # параметр 0 внутри интервала параметров
    assert individual.overstepping()
    individual.code = '101010' # параметр 3 внутри интервала параметров
    assert not individual.overstepping()

def test_new_random_individual(cga_config):
    # Тест на проверку работы Фабрики особей
    from src.classical_genetic_algorithm.model.cga_individual import IndividualFactory
    import random
    random.seed(1)
    individual = IndividualFactory.new_random_individual()
    assert individual.code == '001100'
    assert individual.rank is None