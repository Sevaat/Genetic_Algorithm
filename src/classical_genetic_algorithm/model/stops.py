from copy import deepcopy
from typing import Any, Dict, Tuple, List

from classical_genetic_algorithm.model.individual import Individual
from classical_genetic_algorithm.utils.purpose import get_sorted_population


def stopping_for_the_best(population: List[Individual], best_individual: Individual, counter: int, trend: str) -> tuple[
    Individual, int, bool]:
    """
    Проверка на неизменность лучшей особи на протяжении ряда эпох

    :param population: список особей
    :param best_individual: лучшая найденная особь
    :param counter: количество повторений лучшей особи в популяциях
    :param trend: направление оптимизации (минимум, максимум)

    :return: вывод True, если на протяжении ряда эпох не было изменения лучшей особи
    """

    copy_population = deepcopy(population)

    if best_individual is None:
        best_individual = copy_population[0]
        counter = 0
    else:
        copy_population += [best_individual]
        copy_population = get_sorted_population(copy_population, trend)
        if best_individual == copy_population[0]:
            counter += 1
        else:
            best_individual = copy_population[0]
            counter = 0

    return best_individual, counter, (counter == 10)

def stopping_by_the_number_of_eras(era: int, parameters: Dict[str, Any]) -> bool:
    """
    Останов по количеству эпох

    :param era: номер текущей эры
    :param parameters: параметры ГА

    :return: вывод False
    """

    if era == parameters["number_of_eras"]:
        return True
    return False

def stop_for_homogeneity(population: List[Individual], trend: str) -> bool:
    """
    Останов по однородности популяции

    :param population: список особей
    :param trend: направление оптимизации (минимум, максимум)

    :return:
    """

    copy_population = deepcopy(population)
    copy_population = get_sorted_population(copy_population, trend)

    if copy_population.count(copy_population[0]) / len(copy_population) >= 0.95:
        return True
    return False

def get_stops(population: List[Individual], best_individual: Individual, counter: int, trend: str, era: int, parameters: Dict[str, Any]) -> \
tuple[Individual, int, bool]:
    """Останов"""

    best_individual, counter, stop_1 = stopping_for_the_best(population, best_individual, counter, trend)

    stop_2 = stopping_by_the_number_of_eras(era, parameters)

    stop_3 = stop_for_homogeneity(population, trend)

    return best_individual, counter, stop_1 or stop_2 or stop_3







