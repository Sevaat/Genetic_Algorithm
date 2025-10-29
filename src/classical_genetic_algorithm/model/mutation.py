from abc import ABC
import random
from typing import List

from src.classical_genetic_algorithm.model.individual import Individual
from src.classical_genetic_algorithm.options.parameters import Parameters
from src.classical_genetic_algorithm.utils.duplicate_check import DuplicateCheck


class Mutation(ABC):
    @staticmethod
    def inversion_one_bit(population: List[Individual], children: List[Individual], parameters: Parameters) -> List[Individual]:
        """
        Оператор мутации (изменение параметра особи с некоторой заданной вероятностью)
        :param parameters: параметры ГА
        :param population: список особей
        :param children: список детей
        :return: список особей-мутантов
        """
        mutants = []
        p1 = parameters.mutation_probability * 100
        p2 = 100 - p1
        for child in children:
            new_code = ''
            for c in list(child.code):
                if c == '1':
                    new_code += random.choices(['0', '1'], weights=[p1, p2], k=1)[0]
                else:
                    new_code += random.choices(['0', '1'], weights=[p2, p1], k=1)[0]

            # проверка на корректные значения и дублирование после мутации
            new_individual = Individual.new_individual_by_code(new_code, parameters)
            mutants.append(new_individual)
            if new_individual is not None:
                if DuplicateCheck.individual_addition(population + mutants, new_individual, parameters):
                    mutants.append(new_individual)
        return mutants


    @staticmethod
    def inversion_group_bits():
        """Инверсия группы бит - инвертируется несколько подряд идущих генов"""
        pass


    @staticmethod
    def swap():
        """Обмен - два случайно выбранных гена меняются местами"""
        pass


    @staticmethod
    def reverse():
        """Обращение - случайная последовательность генов записывается в обратном порядке"""
        pass


    @staticmethod
    def shuffle():
        """Перетасовка - значения выбранной непрерывной последовательности генов перемешиваются случайным образом"""
        pass
