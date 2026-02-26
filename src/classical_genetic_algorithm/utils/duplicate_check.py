from typing import List, Dict, Any

from src.classical_genetic_algorithm.model.individual import Individual


def individual_addition(population: List[Individual], individual: Individual, parameters: Dict[str, Any]) -> bool:
    """
    Проверка на количество повторений особи

    :param parameters: параметры ГА
    :param population: список особей
    :param individual: особь, количество которой подсчитывается

    :return: True - если количество вхождений не превышено; False - иначе
    """

    if (
        parameters['number_of_recurring_individuals'] == 0
        or parameters['number_of_recurring_individuals'] > population.count(individual)
    ):
        return True
    else:
        return False
