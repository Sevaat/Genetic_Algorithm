from abc import ABC
from typing import List

from src.classical_genetic_algorithm.model.individual import Individual
from src.classical_genetic_algorithm.options.operators import Operators
from src.classical_genetic_algorithm.options.parameters import Parameters


class Replacement(ABC):
    @staticmethod
    def elite(individuals_1: List[Individual], individuals_2: List[Individual], parameters: Parameters,
              operators: Operators) -> List[Individual]:
        """
        Замена популяции через элитизм (неизменным остаётся % лучших особей)
        :param operators: операторы ГА
        :param parameters: параметры ГА
        :param individuals_1: список особей в начальной популяции
        :param individuals_2: список новых особей-мутантов
        :return: список элитных особей и лучших особей-мутантов в количестве не превышающем максимального значения популяции
        """
        n_elite = int(parameters.proportion_of_elite_individuals * parameters.number_of_individuals)
        if len(individuals_1) - n_elite > len(individuals_2):
            n_elite = len(individuals_1) - n_elite
        new_individuals = individuals_1[:n_elite]
        new_individuals += individuals_2
        new_individuals = operators.purpose(new_individuals)
        new_individuals = new_individuals[:parameters.number_of_individuals]
        return new_individuals

    @staticmethod
    def simple_cut(individuals_1: List[Individual], individuals_2: List[Individual], parameters: Parameters,
                   operators: Operators) -> List[Individual]:
        """
        Замена популяции через отсечения лучших особей
        :param individuals_1: список особей в начальной популяции
        :param individuals_2: список новых особей-мутантов
        :param operators: операторы ГА
        :param parameters: параметры ГА
        :return: список лучших особей и особей-мутантов в количестве не превышающем максимального значения популяции
        """
        new_individuals = individuals_1 + individuals_2
        new_individuals = operators.purpose(new_individuals)
        new_individuals = new_individuals[:parameters.number_of_individuals]
        return new_individuals
