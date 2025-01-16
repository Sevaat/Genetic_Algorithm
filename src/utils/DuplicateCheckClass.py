from abc import ABC
from src.model.IndividualClass import Individual
import src.utils.GlobalVariables as GV


class DuplicateCheck(ABC):
    @staticmethod
    def individual_addition(population: [Individual], individual: Individual) -> bool:
        """
        Проверка на количество повторений особи
        :param population: список особей
        :param individual: особь, количество которой подсчитывается
        :return: True - если количество вхождений не превышено; False - иначе
        """
        if GV.PARAMETERS.number_of_recurring_individuals == 0:
            return True
        else:
            n = 0
            for ind in population:
                if individual.code == ind.code:
                    n += 1
            if GV.PARAMETERS.number_of_recurring_individuals > n:
                return True
            else:
                return False