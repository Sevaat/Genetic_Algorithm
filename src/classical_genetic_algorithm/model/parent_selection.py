from abc import ABC
import random
from typing import List, Tuple, Any

from src.classical_genetic_algorithm.model.individual import Individual
#from src.classical_genetic_algorithm.options.operators import Operators
from src.classical_genetic_algorithm.utils.purpose import Purpose


class Selection(ABC):
    @staticmethod
    def standard_selection(individuals: List[Individual], operators: Any) -> List[Tuple[Individual, Individual]]:
        """
        Выбор родителей в соответствии с весом (значение ЦФ)
        :param operators: операторы ГА
        :param individuals: список взвешенных (со значением ЦФ) особей
        :return: список родителей длиной len(individuals) по 2 особи
        """
        weights = Selection.get_weights(individuals, operators)
        parents = []
        while len(parents) < int(len(individuals)):
            p_1, p_2 = random.choices(individuals, weights=weights, k=2)
            if p_1.code != p_2.code:
                parents.append((p_1, p_2))
            else:
                continue
        return parents

    @staticmethod
    def stochastic_universal_sampling(individuals: List[Individual], operators: Any) -> list[
        tuple[Individual, Individual]]:
        """
        Выбор родителей с помощью стохастической универсальной выборки (1 - случайно; 3 - со смещением в четверть)
        :param operators: операторы ГА
        :param individuals: список взвешенных (со значением ЦФ) особей
        :return: список родителей длиной len(individuals) по 2 особи
        """
        weights = Selection.get_weights(individuals, operators)
        total_weight = sum(weights)
        pointer_distance = total_weight / 4
        parents = []
        while len(parents) < int(len(individuals)):
            points = [random.uniform(0, total_weight)]
            new_point = points[0]
            for i in range(3):
                new_point += pointer_distance
                if new_point > total_weight:
                    new_point = 0 + new_point - total_weight
                points.append(new_point)
            points = sorted(points)
            j = 0
            current_weight = 0
            new_parents = []
            for i, w in enumerate(weights):
                current_weight += w
                if current_weight >= points[j]:
                    new_parents.append(individuals[i])
                    j += 1
                if j == len(points):
                    break
            for i, p1 in enumerate(new_parents):
                for p2 in new_parents[i + 1:]:
                    parents.append((p1, p2))
        return parents

    @staticmethod
    def get_weights(individuals: List[Individual], operators: Any) -> List[float]:
        """
        Получение весов для определения родителей по значению ЦФ и цели оптимизации
        :param operators: операторы ГА
        :param individuals: список особей (потенциальных родителей)
        :return: список относительных весов пропорциональных значению ЦФ
        """
        weights = []
        total_weight = sum([p.rank for p in individuals])
        if operators.purpose == Purpose.sort_by_less:
            weights = [p.rank / total_weight for p in individuals]
        if operators.purpose == Purpose.sort_by_more:
            weights = [(total_weight - p.rank) / total_weight for p in individuals]
        return weights
