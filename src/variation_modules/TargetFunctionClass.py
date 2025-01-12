from abc import ABC
from src.model.IndividualClass import *
import src.utils.GlobalVariables as GV
import sys


class TargetFunction(ABC):
    @staticmethod
    def get_result_test_function(individuals: [Individual]) -> [Individual]:
        """
        Тестовая функция суммы значений хромосом
        :param individuals: список особей
        :return: список особей без некорректных (значение хромосомы выходит за допустимые границы)
        """
        new_individuals = []
        for ind in individuals:
            if ind.overstepping():
                rank = 0
                for chromosome in ind.transcript_individual():
                    rank += float(chromosome)
                ind.rank = rank
                new_individuals.append(ind)
        return new_individuals

    @staticmethod
    def get_result_user_defined_function(individuals: [Individual]) -> [Individual]:
        """
        Пользовательская целевая функция
        :param individuals: список особей
        :return: список особей без некорректных (значение хромосомы выходит за допустимые границы)
        """
        new_individuals = []
        for ind in individuals:
            if ind.overstepping():
                individual_parameters = ind.transcript_individual()
                try:
                    ind.rank = GV.GENETIC_ALGORITHM.user_function_reference(individual_parameters)
                except:
                    print('Введена некорректная функция или функция принимает некорректные аргументы.')
                    print('Проверьте правильность введенной информации и повторите попытку.')
                    sys.exit()
                new_individuals.append(ind)
        return new_individuals


if __name__ == '__main__':
    pass
