from abc import ABC
from typing import Union

from src.classical_genetic_algorithm.model.cga_individual import Individual


class Stops(ABC):
    @staticmethod
    def stopping_for_the_best(individuals: [Individual]) -> Union[bool, None]:
        """
        Проверка на неизменность лучшей особи на протяжении ряда эпох
        :param individuals: список отсортированных особей
        :return: вывод True, если на протяжении ряда эпох не было изменения лучшей особи
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        if config.best_individual is None:
            config.best_individual = individuals[0]
        elif individuals[0] == config.best_individual:
            config.counter -= 1
            return config.counter == 0
        else:
            config.counter = config.parameters.change_counter
            config.best_individual = individuals[0]

    @staticmethod
    def stopping_by_the_number_of_eras(individuals: [Individual]) -> bool:
        """
        Останов по количеству эпох имеется по-умолчанию
        :param individuals: список отсортированных особей
        :return: вывод False
        """
        return False
