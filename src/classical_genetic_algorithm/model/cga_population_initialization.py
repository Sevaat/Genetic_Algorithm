from abc import ABC
from src.classical_genetic_algorithm.model.cga_individual import IndividualFactory, Individual
from src.classical_genetic_algorithm.utils.cga_duplicate_check import DuplicateCheck


class Population(ABC):
    @staticmethod
    def get_new_random_population() -> [Individual]:
        """
        Создание новой случайной популяции без повторений
        :return: список особей
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        population = []
        while len(population) < config.parameters.number_of_individuals:
            individual = IndividualFactory.new_random_individual()
            if DuplicateCheck.individual_addition(population, individual):
                population.append(individual)
        return population