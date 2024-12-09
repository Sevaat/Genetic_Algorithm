from abc import ABC
import src.utils.GlobalVariables as GV
from src.model.IndividualClass import Individual


class Stops(ABC):
    @staticmethod
    def stopping_for_the_best(individuals: [Individual]) -> bool:
        """
        Проверка на неизменность лучшей особи на протяжении ряда эпох
        :param individuals: список отсортированных особей
        :return: вывод True, если на протяжении ряда эпох не было изменения лучшей особи
        """
        if GV.best_individual is None:
            GV.best_individual = individuals[0]
        elif individuals[0].code == GV.best_individual.code:
            GV.counter -= 1
            return GV.counter == 0
        else:
            GV.counter = GV.PARAMETERS.change_counter
            GV.best_individual = individuals[0]

    @staticmethod
    def stopping_by_the_number_of_eras(individuals: [Individual]) -> bool:
        """
        Останов по количеству эпох имеется по-умолчанию
        :param individuals: список отсортированных особей
        :return: вывод True
        """
        return True


if __name__ == '__main__':
    pass
