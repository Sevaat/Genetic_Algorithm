import random
from typing import Union, Self, List, Dict, Any

#from src.classical_genetic_algorithm.options.parameters import Parameters
from src.classical_genetic_algorithm.utils.gray_code_converter import GrayCodeConverter


class Individual:
    def __init__(self):
        self.code = None    # код Грея особи
        self.rank = None    # значение функции приспособленности

    def __eq__(self, other):
        return self.code == other.code

    def __ne__(self, other):
        return self.code != other.code

    def __str__(self):
        return str(self.code)

    def __repr__(self):
        return str(self.code)

    def to_dict(self, parameters: Any) -> Dict[str, Any]:
        """
        Вывод особи в виде словаря
        :param parameters: параметры ГА
        :return: словарь описания особи
        """
        return {'code': self.code, 'rank': self.rank, 'genotype': self.transcript_individual(parameters)}

    def transcript_individual(self, parameters: Any) -> List[str]:
        """
        Перевод кода особи в список параметров
        :param parameters: параметры ГА
        :return: список параметров
        """
        genotype = GrayCodeConverter.convert_from_code(self.code, parameters)
        genotype = [parameters.gene_sets[i][p] for i, p in enumerate(genotype)]
        return genotype

    def overstepping(self, parameters: Any) -> bool:
        """
        Проверка допустимости параметров особи (нахождение в допустимых пределах)
        :param parameters: параметры ГА
        :return: True - если в допустимых пределах, False - иначе
        """
        genotype = GrayCodeConverter.convert_from_code(self.code, parameters)
        flag = True
        for i, gene in enumerate(genotype):
            if gene >= len(parameters.gene_sets[i]):
                flag = False
                break
        return flag

    @classmethod
    def new_individual_by_code(cls, code: str, parameters: Any) -> Union[Self, None]:
        """
        Создание особи по коду Грея
        :param code: код Грея особи
        :param parameters: параметры ГА
        :return: особь
        """
        individual = cls()
        individual.code = code
        if individual.overstepping(parameters):
            return individual
        else:
            return None

class IndividualFactory:
    @staticmethod
    def new_random_individual(parameters: Any) -> Individual:
        """
        Фабрика для производства случайных особей
        :param parameters: параметры ГА
        :return: случайная особь
        """
        individual = Individual()
        new_genotype = []
        for gene_set in parameters.gene_sets:
            individual_chromosome = random.randint(0, len(gene_set) - 1)
            new_genotype.append(individual_chromosome)
        individual.code = GrayCodeConverter.convert_to_code(new_genotype, parameters)
        return individual
