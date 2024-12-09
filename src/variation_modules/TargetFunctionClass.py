from abc import ABC
from src.model.IndividualClass import *


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
                    rank += int(chromosome)
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
                '''
                Здесь определяется пользовательская ЦФ
                Результат целевой функции должен быть выражен численным значением
                Значение ЦФ записывается в переменную rank, определенную ниже
                '''
                rank = 0
                ind.rank = rank
                new_individuals.append(ind)
        return new_individuals


if __name__ == '__main__':
    pass
