from src.utils.data_verification import DataVerification
from typing import List, Any



class Parameters:
    def __init__(self):
        self.__number_of_individuals = None  # количество особей в популяции
        self.__proportion_of_elite_individuals = None  # доля элитных особей
        self.__number_of_eras = None  # количество эпох
        self.__gene_sets = None  # данные хромосом
        self.__mutation_probability = None  # вероятность мутации
        self.__change_counter = None # счётчик изменений лучшей особи
        self.__number_of_results = None # количество выводимых результатов
        self.__recombination_point_count = None # количество точек рекомбинации
        self.__number_of_recurring_individuals = 0 # количество повторяющихся особей

    @property
    def number_of_individuals(self):
        return self.__number_of_individuals

    @number_of_individuals.setter
    def number_of_individuals(self, value: str):
        self.__number_of_individuals = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def proportion_of_elite_individuals(self):
        return self.__proportion_of_elite_individuals

    @proportion_of_elite_individuals.setter
    def proportion_of_elite_individuals(self, value: str):
        self.__proportion_of_elite_individuals = DataVerification.verification(value, 'float', 0, 1, False, False)

    @property
    def number_of_eras(self):
        return self.__number_of_eras

    @number_of_eras.setter
    def number_of_eras(self, value: str):
        self.__number_of_eras = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def mutation_probability(self):
        return self.__mutation_probability

    @mutation_probability.setter
    def mutation_probability(self, value: str):
        self.__mutation_probability = DataVerification.verification(value, 'float', 0, 1, False, False)

    @property
    def change_counter(self):
        return self.__change_counter

    @change_counter.setter
    def change_counter(self, value: str):
        self.__change_counter = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def number_of_results(self):
        return self.__number_of_results

    @number_of_results.setter
    def number_of_results(self, value: str):
        self.__number_of_results = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def recombination_point_count(self):
        return self.__recombination_point_count

    @recombination_point_count.setter
    def recombination_point_count(self, value: str):
        self.__recombination_point_count = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def number_of_recurring_individuals(self):
        return self.__number_of_recurring_individuals

    @number_of_recurring_individuals.setter
    def number_of_recurring_individuals(self, value: str):
        self.__number_of_recurring_individuals = DataVerification.verification(value, 'int', 0, float('inf'), False, True)

    @property
    def gene_sets(self):
        return self.__gene_sets

    @gene_sets.setter
    def gene_sets(self, value: List[List[Any]]):
        self.__gene_sets = value

