import random
from src.utils.GrayCodeConverterClass import GrayCodeConverter
import src.utils.GlobalVariables as GV


class Individual:
    def __init__(self):
        self.code = None
        self.rank = None

    def __str__(self):
        return f'Код: {self.code}. Значение ЦФ: {self.rank}. Генотип: {self.transcript_individual()}'

    def transcript_individual(self) -> [str]:
        """
        Перевод кода особи в список параметров
        :return: список параметров
        """
        genotype = GrayCodeConverter.convert_from_code(self.code)
        genotype = [GV.PARAMETERS.gene_sets[i][p] for i, p in enumerate(genotype)]
        return genotype

    def overstepping(self) -> bool:
        """
        Проверка допустимости параметров особи (нахождение в допустимых пределах)
        :return: True - если в допустимых пределах, False - иначе
        """
        genotype = GrayCodeConverter.convert_from_code(self.code)
        flag = True
        for i, gene in enumerate(genotype):
            if gene >= len(GV.PARAMETERS.gene_sets[i]):
                flag = False
                break
        return flag

    @staticmethod
    def new_individual_by_code(code):
        """
        Создание особи по коду Грея
        :param code: код Грея особи
        :return: особь
        """
        individual = Individual()
        individual.code = code
        return individual

class IndividualFactory:
    @staticmethod
    def new_random_individual():
        """
        Фабрика для производства случайных особей
        :return: случайная особь
        """
        individual = Individual()
        new_genotype = []
        for gene_set in GV.PARAMETERS.gene_sets:
            individual_chromosome = random.randint(0, len(gene_set) - 1)
            new_genotype.append(individual_chromosome)
        individual.code = GrayCodeConverter.convert_to_code(new_genotype)
        return individual


if __name__ == '__main__':
    pass
