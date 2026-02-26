from typing import List, Dict, Any, Callable

from src.classical_genetic_algorithm.model.individual import Individual, IndividualFactory
from src.classical_genetic_algorithm.utils.duplicate_check import DuplicateCheck


def get_new_random_population(parameters: Dict[str, Any]) -> List[Individual]:
    """
    Создание новой случайной популяции без повторений
    :param parameters: параметры ГА
    :return: список особей
    """
    population: List[Individual] = []
    while len(population) < parameters['number_of_individuals']:
        individual = IndividualFactory.new_random_individual(parameters)
        if DuplicateCheck.individual_addition(population, individual, parameters):
            population.append(individual)
    return population


def get_population_initialization(data: Dict[str, Any]) -> Callable:
    """Получить метод инициализации начальной популяции по исходным данным"""

    if 'population_initialization' not in data['operators']:
        raise KeyError('В исходных данных отсутствует информация по операторам ГА (operators/population_initialization)')
    methods = {
        "random": get_new_random_population,
    }
    if data['operators']['population_initialization'] in methods.keys():
        return methods[data['operators']['population_initialization']]
    else:
        raise KeyError('В исходных данных отсутствует информация по операторам ГА (operators/population_initialization/method)')
