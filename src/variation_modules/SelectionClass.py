from abc import ABC
import random
from src.model.IndividualClass import Individual


class Selection(ABC):
    @staticmethod
    def standart_selection(individuals: [Individual]) -> [Individual]:
        """
        Выбор родителей в соответствии с весом (значение ЦФ)
        :param individuals: список взвешенных (со значением ЦФ) особей
        :return: список родителей (int(len(individuals)/2) на 2)
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
        Выбор родителей с помощью стохастической универсальной выборке (1 - случайно; 3 - со смещением в четверть)
        :param individuals: список взвешенных (со значением ЦФ) особей
        :return: список родителей (int(len(individuals)/6) на 4)
        """
        weights = [p.rating for p in individuals]
        total_weight = sum(weights)
        pointer_distance = total_weight / 4
        parents = []
        while len(parents) < int(len(individuals)/6):
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
            parents.append(new_parents)
        return parents


if __name__ == '__main__':
    pass
