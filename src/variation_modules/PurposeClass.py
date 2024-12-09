from abc import ABC
from src.model.IndividualClass import Individual


class Purpose(ABC):
    @staticmethod
    def sort_by_more(individuals: [Individual]) -> [Individual]:
        """
        Сортировка особей по значению ЦФ: от меньшего к большему
        :param individuals: список особей
        :return: сортированный список особей от меньшего к большему
        """
        individuals = sorted(individuals, key=lambda ind: ind.rank)
        return individuals

    @staticmethod
    def sort_by_less(individuals: [Individual]) -> [Individual]:
        """
        Сортировка особей по значению ЦФ: от большего к меньшему
        :param individuals: список особей
        :return: сортированный список особей от большего к меньшему
        """
        individuals = sorted(individuals, key=lambda ind: ind.rank)
        individuals.reverse()
        return individuals


if __name__ == '__main__':
    pass
