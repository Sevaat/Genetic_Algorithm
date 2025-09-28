from abc import ABC
import random
from src.classical_genetic_algorithm.model.cga_individual import Individual
from src.classical_genetic_algorithm.utils.cga_duplicate_check import DuplicateCheck


class Mutation(ABC):
    @staticmethod
    def mutation(population: [Individual], children: [Individual]) -> [Individual]:
        """
        Оператор мутации (изменение параметра особи с некоторой заданной вероятностью)
        :param population: список особей
        :param children: список детей
        :return: список особей-мутантов
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        mutants = []
        p1 = config.parameters.mutation_probability * 100
        p2 = 100 - p1
        for child in children:
            new_code = ''
            for c in list(child.code):
                if c == '1':
                    new_code += random.choices(['0', '1'], weights=[p1, p2], k=1)[0]
                else:
                    new_code += random.choices(['0', '1'], weights=[p2, p1], k=1)[0]

            # проверка на корректные значения и дублирование после мутации
            new_individual = Individual.new_individual_by_code(new_code)
            if new_individual is not None:
                if DuplicateCheck.individual_addition(population, new_individual):
                    mutants.append(new_individual)
        return mutants
