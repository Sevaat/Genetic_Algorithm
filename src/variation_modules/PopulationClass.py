from abc import ABC
from src.model.IndividualClass import *
from src.utils.DuplicateCheckClass import DuplicateCheck


class Population(ABC):
    @staticmethod
    def get_new_random_population() -> [Individual]:
        """
        Создание новой случайной популяции без повторений
        :return: список особей
        """
        population = []
        while len(population) < GV.PARAMETERS.number_of_individuals:
            individual = IndividualFactory.new_random_individual()
            if DuplicateCheck.individual_addition(population, individual):
                population.append(individual)
        return population


if __name__ == '__main__':
    pass
