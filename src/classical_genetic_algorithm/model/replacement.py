from copy import deepcopy
from typing import Any, Callable, Dict, List

from classical_genetic_algorithm.utils.purpose import get_sorted_population
from src.classical_genetic_algorithm.model.individual import Individual


def elite(
    population: List[Individual], mutants: List[Individual], parameters: Dict[str, Any], trend: str
) -> List[Individual]:
    """
    Замена популяции через элитизм (неизменным остаётся % лучших особей)

    :param trend: сортировщик по убыванию или возрастанию
    :param parameters: параметры ГА
    :param population: список особей в начальной популяции
    :param mutants: список новых особей-мутантов

    :return: список элитных особей и лучших особей-мутантов в количестве не превышающем макс. значения популяции
    """

    if not population:
        raise KeyError("Список особей пуст")

    n_elite = int(parameters["proportion_of_elite_individuals"] * parameters["number_of_individuals"])

    if len(population) - n_elite > len(mutants):
        n_elite = len(population) - len(mutants)

    new_individuals = deepcopy(population[:n_elite])
    new_individuals += deepcopy(mutants)
    new_individuals = get_sorted_population(new_individuals, trend)

    return new_individuals[: parameters["number_of_individuals"]]


def simple_cut(
    population: List[Individual], mutants: List[Individual], parameters: Dict[str, Any], trend: str
) -> List[Individual]:
    """
    Замена популяции через отсечения лучших особей

    :param population: список особей в начальной популяции
    :param mutants: список новых особей-мутантов
    :param trend: сортировщик по убыванию или возрастанию
    :param parameters: параметры ГА

    :return: список лучших особей и особей-мутантов в количестве не превышающем максимального значения популяции
    """

    if not population:
        raise KeyError("Список особей пуст")

    new_individuals = deepcopy(population) + deepcopy(mutants)
    new_individuals = get_sorted_population(new_individuals, trend)

    return new_individuals[: parameters["number_of_individuals"]]


def get_replacement(data: Dict[str, Any]) -> Callable:
    """Получить метод сохранения особей по исходным данным"""

    if "replacement" not in data["operators"]:
        raise KeyError("В исходных данных отсутствует информация по операторам ГА (operators/replacement)")
    methods = {
        "elite": elite,
        "easy_cut": simple_cut,
    }
    if data["operators"]["replacement"] in methods.keys():
        return methods[data["operators"]["replacement"]]
    else:
        raise KeyError("В исходных данных отсутствует информация по операторам ГА (operators/replacement/method)")
