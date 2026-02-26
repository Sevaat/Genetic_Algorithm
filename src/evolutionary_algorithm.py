from abc import ABC
from typing import Callable

from src.classical_genetic_algorithm.classical_genetic_algorithm import CGA


class EvolutionaryAlgorithm(ABC):
    @staticmethod
    def classical_genetic_algorithm() -> None:
        """
        Оптимизация с использованием классического генетического алгоритма

        :return:
        """

        cga = CGA()
        cga.run()
