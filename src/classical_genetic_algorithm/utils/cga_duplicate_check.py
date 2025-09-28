from abc import ABC
from src.classical_genetic_algorithm.model.cga_individual import Individual


class DuplicateCheck(ABC):
    @staticmethod
    def individual_addition(population: [Individual], individual: Individual) -> bool:
        """
        Проверка на количество повторений особи
        :param population: список особей
        :param individual: особь, количество которой подсчитывается
        :return: True - если количество вхождений не превышено; False - иначе
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        if config.parameters.number_of_recurring_individuals == 0:
            return True
        else:
            n = 0
            for ind in population:
                if individual == ind:
                    n += 1
            if config.parameters.number_of_recurring_individuals > n:
                return True
            else:
                return False