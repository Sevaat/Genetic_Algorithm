from src.classical_genetic_algorithm.utils.cga_data_verification import DataVerification
from typing import List

class Parameters:
    def __init__(self):
        self._number_of_individuals = None                  # количество особей в популяции
        self._proportion_of_elite_individuals = None        # доля элитных особей
        self._number_of_eras = None                         # количество эпох
        self._gene_sets = None                              # данные хромосом
        self._mutation_probability = None                   # вероятность мутации
        self._change_counter = None                         # счётчик изменений лучшей особи
        self._number_of_results = None                      # количество выводимых результатов
        self._recombination_point_count = None              # количество точек рекомбинации
        self._number_of_recurring_individuals = None        # количество повторяющихся особей (0 - сколько угодно)

    @property
    def number_of_individuals(self):
        return self._number_of_individuals

    @number_of_individuals.setter
    def number_of_individuals(self, value: str):
        self._number_of_individuals = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def proportion_of_elite_individuals(self):
        return self._proportion_of_elite_individuals

    @proportion_of_elite_individuals.setter
    def proportion_of_elite_individuals(self, value: str):
        self._proportion_of_elite_individuals = DataVerification.verification(value, 'float', 0, 1, False, False)

    @property
    def number_of_eras(self):
        return self._number_of_eras

    @number_of_eras.setter
    def number_of_eras(self, value: str):
        self._number_of_eras = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def mutation_probability(self):
        return self._mutation_probability

    @mutation_probability.setter
    def mutation_probability(self, value: str):
        self._mutation_probability = DataVerification.verification(value, 'float', 0, 1, False, False)

    @property
    def change_counter(self):
        return self._change_counter

    @change_counter.setter
    def change_counter(self, value: str):
        self._change_counter = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def number_of_results(self):
        return self._number_of_results

    @number_of_results.setter
    def number_of_results(self, value: str):
        self._number_of_results = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def recombination_point_count(self):
        return self._recombination_point_count

    @recombination_point_count.setter
    def recombination_point_count(self, value: str):
        self._recombination_point_count = DataVerification.verification(value, 'int', 0, float('inf'), True, True)

    @property
    def number_of_recurring_individuals(self):
        return self._number_of_recurring_individuals

    @number_of_recurring_individuals.setter
    def number_of_recurring_individuals(self, value: str):
        self._number_of_recurring_individuals = DataVerification.verification(value, 'int', 0, float('inf'), False, True)

    @property
    def gene_sets(self):
        return self._gene_sets

    @gene_sets.setter
    def gene_sets(self, data_gene_sets: dict[str, list[str]]):
        gene_sets = []
        for gs in data_gene_sets["simple set"]:
            gene_sets.append(gs.split())
        for gs in data_gene_sets["step set"]:
            gene_set = []
            start, end, step = gs[2:].strip().split()
            if DataVerification.is_float(start) and DataVerification.is_float(end) and DataVerification.is_float(step):
                start, end, step = float(start), float(end), float(step)
            while start <= end:
                gene_set.append(str(start))
                start += step
            gene_sets.append(gene_set)
        self._gene_sets = gene_sets

def get_parameters(data_parameters: dict) -> Parameters:
    """
    Сборка экземпляра класса параметров
    :param data_parameters: входной список параметров
    :return: параметры ГА
    """
    parameters = Parameters()
    parameters.number_of_individuals = data_parameters['number of individuals']
    parameters.proportion_of_elite_individuals = data_parameters['proportion of elite individuals']
    parameters.number_of_eras = data_parameters['number of eras']
    parameters.gene_sets = data_parameters['gene sets']
    parameters.mutation_probability = data_parameters['mutation probability']
    parameters.change_counter = data_parameters['change counter']
    parameters.number_of_results = data_parameters['number of results']
    parameters.recombination_point_count = data_parameters['recombination point count']
    parameters.number_of_recurring_individuals = data_parameters['number of recurring individuals']
    return parameters