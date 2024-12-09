from abc import ABC
from src.model.IndividualClass import Individual
import src.utils.GlobalVariables as GV


class Replacement(ABC):
    @staticmethod
    def elite(individuals_1: [Individual], individuals_2: [Individual]) -> [Individual]:
        """
        Замена популяции через элитизм (неизменным остаётся % лучших особей)
        :param individuals_1: список особей в начальной популяции
        :param individuals_2: список новых особей-мутантов
        :return: список элитных особей и лучших особей-мутантов в количестве не превышающем максимального значения популяции
        """
        n_elite = int(GV.PARAMETERS.proportion_of_elite_individuals * GV.PARAMETERS.number_of_individuals)
        individuals_1 = individuals_1[:n_elite]
        individuals_1 += individuals_2
        individuals_1 = GV.GENETIC_ALGORITHM.purpose(individuals_1)
        individuals_1 = individuals_1[:GV.PARAMETERS.number_of_individuals]
        return individuals_1

    @staticmethod
    def simple_cut(individuals_1: [Individual], individuals_2: [Individual]) -> [Individual]:
        """
        Замена популяции через отсечения лучших особей
        :param individuals_1: список особей в начальной популяции
        :param individuals_2: список новых особей-мутантов
        :return: список лучших особей и особей-мутантов в количестве не превышающем максимального значения популяции
        """
        individuals_1 += individuals_2
        individuals_1 = GV.GENETIC_ALGORITHM.purpose(individuals_1)
        individuals_1 = individuals_1[:GV.PARAMETERS.number_of_individuals]
        return individuals_1
    
    
if __name__ == '__main__':
    pass