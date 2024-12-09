from abc import ABC
from src.model.IndividualClass import *


class Population(ABC):
    @staticmethod
    def get_new_random_population() -> [Individual]:
        """
        Создание новой случайной популяции
        :return: список особей
        """
        population = []
        while len(population) < GV.PARAMETERS.number_of_individuals:
            individual = IndividualFactory.new_random_individual()
            population.append(individual)
        return population


if __name__ == '__main__':
    pass
