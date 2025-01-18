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
        if len(individuals_1)-n_elite > len(individuals_2):
            n_elite = len(individuals_1)-n_elite
        new_individuals = individuals_1[:n_elite]
        new_individuals += individuals_2
        new_individuals = GV.GENETIC_ALGORITHM.purpose(new_individuals)
        new_individuals = new_individuals[:GV.PARAMETERS.number_of_individuals]
        return new_individuals

    @staticmethod
    def simple_cut(individuals_1: [Individual], individuals_2: [Individual]) -> [Individual]:
        """
        Замена популяции через отсечения лучших особей
        :param individuals_1: список особей в начальной популяции
        :param individuals_2: список новых особей-мутантов
        :return: список лучших особей и особей-мутантов в количестве не превышающем максимального значения популяции
        """
        new_individuals = individuals_1 + individuals_2
        new_individuals = GV.GENETIC_ALGORITHM.purpose(new_individuals)
        new_individuals = new_individuals[:GV.PARAMETERS.number_of_individuals]
        return new_individuals
    
    
if __name__ == '__main__':
    pass