import random
from copy import deepcopy
from typing import Any, Callable, Dict, List, Tuple

from src.classical_genetic_algorithm.model.individual import Individual


def get_weights(population: List[Individual], trend: str) -> List[float]:
    """
    Получение весов для определения родителей по значению ЦФ и цели оптимизации

    :param trend: убывание или возрастание
    :param population: список особей (потенциальных родителей)

    :return: список относительных весов пропорциональных значению ЦФ
    """

    if not population:
        raise KeyError("Список особей пуст")

    ranks = [p.rank for p in population]
    min_rank = min(ranks)
    max_rank = max(ranks)

    if min_rank == max_rank:
        return [1.0 / len(population)] * len(population)

    scaled = []
    if trend == "maximum":
        # Масштабируем в [0, 1] где max_rank -> 1, min_rank -> 0
        scaled = [(r - min_rank) / (max_rank - min_rank) for r in ranks]

    elif trend == "minimum":
        # Масштабируем в [0, 1] где min_rank -> 1, max_rank -> 0
        scaled = [(max_rank - r) / (max_rank - min_rank) for r in ranks]

    epsilon = 1e-10
    scaled = [s + epsilon for s in scaled]

    total = sum(scaled)
    weights = [s / total for s in scaled]

    return weights


def standard_selection(population: List[Individual], trend: str) -> List[Tuple[Individual, Individual]]:
    """
    Выбор родителей в соответствии с весом (значение ЦФ)

    :param trend: убывание или возрастание
    :param population: список взвешенных (со значением ЦФ) особей

    :return: список родителей длиной len(individuals) по 2 особи
    """

    if not population:
        raise KeyError("Список особей пуст")

    current_population = deepcopy(population)

    weights = get_weights(current_population, trend)

    parents: List[Tuple[Individual, Individual]] = []

    while len(parents) < len(current_population):
        p_1, p_2 = random.choices(current_population, weights=weights, k=2)
        if p_1.code != p_2.code:
            parents.append((p_1, p_2))
        else:
            continue

    return parents


def stochastic_universal_sampling(population: List[Individual], trend: str) -> list[tuple[Individual, Individual]]:
    """
    Выбор родителей с помощью стохастической универсальной выборки (1 - случайно; 3 - со смещением в четверть оси)
    1 родитель выбирается случайно (вероятность p),
    2 родитель выбирается как p+0,25,
    3 родитель - p+0,5,
    4 родитель - p+0.75

    :param trend: сортировщик по убыванию или возрастанию
    :param population: список взвешенных (со значением ЦФ) особей

    :return: список родителей длиной len(individuals) по 2 особи
    """

    if not population:
        raise KeyError("Список особей пуст")

    current_population = deepcopy(population)

    weights = get_weights(current_population, trend)
    total_weight = sum(weights)
    pointer_distance = total_weight / 4
    parents: List[Tuple[Individual, Individual]] = []

    while len(parents) < len(current_population):
        points = [random.uniform(0, total_weight)]
        new_point = points[0]

        for i in range(3):
            new_point += pointer_distance
            if new_point > total_weight:
                new_point = 0 + new_point - total_weight
            points.append(new_point)
        points = sorted(points)

        j = 0
        current_weight: float = 0
        new_parents = []
        for i, w in enumerate(weights):
            current_weight += w
            if current_weight >= points[j]:
                new_parents.append(current_population[i])
                j += 1
            if j == len(points):
                break

        for i, p1 in enumerate(new_parents):
            for p2 in new_parents[i + 1 :]:
                parents.append((p1, p2))

    return parents


def get_parent_selection(data: Dict[str, Any]) -> Callable:
    """Получить метод выбора родителей по исходным данным"""

    if "parent_selection" not in data["operators"]:
        raise KeyError("В исходных данных отсутствует информация по операторам ГА (operators/parent_selection)")
    methods = {
        "standard": standard_selection,
        "stochastic_universal_sampling": stochastic_universal_sampling,
    }
    if data["operators"]["parent_selection"] in methods.keys():
        return methods[data["operators"]["parent_selection"]]
    else:
        raise KeyError("В исходных данных отсутствует информация по операторам ГА (operators/parent_selection/method)")
