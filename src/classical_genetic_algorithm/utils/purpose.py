from copy import deepcopy
from typing import List

from src.classical_genetic_algorithm.model.individual import Individual


def sort_by_more(population: List[Individual]) -> List[Individual]:
    """
    Сортировка особей по значению ЦФ: от меньшего к большему

    :param population: список особей

    :return: сортированный список особей от меньшего к большему
    """

    if not population:
        raise KeyError("Список особей пуст")

    sorted_population = deepcopy(population)

    sorted_population = sorted(sorted_population, key=lambda ind: ind.rank)

    return sorted_population


def sort_by_less(population: List[Individual]) -> List[Individual]:
    """
    Сортировка особей по значению ЦФ: от большего к меньшему

    :param population: список особей

    :return: сортированный список особей от большего к меньшему
    """

    if not population:
        raise KeyError("Список особей пуст")

    sorted_population = deepcopy(population)

    sorted_population = sorted(sorted_population, key=lambda ind: ind.rank, reverse=True)

    return sorted_population


def get_sorted_population(population: List[Individual], trend: str) -> List[Individual]:
    """Получить отсортированную популяцию"""

    if trend == "minimum":
        return sort_by_more(population)
    elif trend == "maximum":
        return sort_by_less(population)

    return population
