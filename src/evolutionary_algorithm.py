from abc import ABC
from typing import Callable

from src.classical_genetic_algorithm.classical_genetic_algorithm import CGA


class EvolutionaryAlgorithm(ABC):
    @staticmethod
    def classical_genetic_algorithm(user_function: Callable) -> None:
        """
        Оптимизация с использованием классического генетического алгоритма
        :param user_function: пользовательская целевая функция, с помощью которой оцениваются решения
        :return:
        """
        cga = CGA(user_function)
        cga.run()
