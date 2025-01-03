from abc import ABC
import random
from src.model.IndividualClass import Individual


class Selection(ABC):
    @staticmethod
    def standart_selection(individuals: [Individual]) -> [Individual]:
        """
        Выбор родителей в соответствии с весом (значение ЦФ)
        :param individuals: список взвешенных (со значением ЦФ) особей
        :return: список родителей длиной len(individuals)/2 по 2 особи
        """
        weights = [p.rank for p in individuals]
        parents = []
        while len(parents) < int(len(individuals)/2):
            p_1, p_2 = random.choices(individuals, weights=weights, k=2)
            if p_1.code != p_2.code:
                parents.append([p_1, p_2])
            else:
                continue
        return parents

    @staticmethod
    def stochastic_universal_sampling(individuals: [Individual]) -> [Individual]:
        """
        Выбор родителей с помощью стохастической универсальной выборки (1 - случайно; 3 - со смещением в четверть)
        :param individuals: список взвешенных (со значением ЦФ) особей
        :return: список родителей длиной len(individuals)/2 по 2 особи
        """
        weights = [p.rating for p in individuals]
        total_weight = sum(weights)
        pointer_distance = total_weight / 4
        parents = []
        while len(parents) < int(len(individuals)/2):
            points = [random.uniform(0, total_weight)]
            new_point = points[0]
            for i in range(3):
                new_point += pointer_distance
                if new_point > total_weight:
                    new_point = 0 + new_point - total_weight
                else:
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
            for i, p1 in enumerate(new_parents):
                for p2 in new_parents[i + 1:]:
                    parents.append([p1, p2])
        return parents


if __name__ == '__main__':
    pass
