import random
from typing import Union, Self

from src.classical_genetic_algorithm.utils.cga_gray_code_converter import GrayCodeConverter


class Individual:
    def __init__(self):
        self.code = None    # код Грея особи
        self.rank = None    # значение функции приспособленности

    def __str__(self):
        return f'Код: {self.code}. Значение ЦФ: {self.rank}. Генотип: {self.transcript_individual()}'

    def __repr__(self):
        return f'Код: {self.code}. Значение ЦФ: {self.rank}. Генотип: {self.transcript_individual()}'

    def __eq__(self, other):
        return self.code == other.code

    def __ne__(self, other):
        return self.code != other.code

    def transcript_individual(self) -> [str]:
        """
        Перевод кода особи в список параметров
        :return: список параметров
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        genotype = GrayCodeConverter.convert_from_code(self.code)
        genotype = [config.parameters.gene_sets[i][p] for i, p in enumerate(genotype)]
        return genotype

    def overstepping(self) -> bool:
        """
        Проверка допустимости параметров особи (нахождение в допустимых пределах)
        :return: True - если в допустимых пределах, False - иначе
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        genotype = GrayCodeConverter.convert_from_code(self.code)
        flag = True
        for i, gene in enumerate(genotype):
            if gene >= len(config.parameters.gene_sets[i]):
                flag = False
                break
        return flag

    @classmethod
    def new_individual_by_code(cls, code: str) -> Union[Self, None]:
        """
        Создание особи по коду Грея
        :param code: код Грея особи
        :return: особь
        """
        individual = cls()
        individual.code = code
        if individual.overstepping():
            return individual
        else:
            return None

class IndividualFactory:
    @staticmethod
    def new_random_individual():
        """
        Фабрика для производства случайных особей
        :return: случайная особь
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        individual = Individual()
        new_genotype = []
        for gene_set in config.parameters.gene_sets:
            individual_chromosome = random.randint(0, len(gene_set) - 1)
            new_genotype.append(individual_chromosome)
        individual.code = GrayCodeConverter.convert_to_code(new_genotype)
        return individual
