from abc import ABC
import random
from src.model.IndividualClass import Individual
import src.utils.GlobalVariables as GV
from src.utils.DuplicateCheckClass import DuplicateCheck


class Mutation(ABC):
    @staticmethod
    def mutation(population: [Individual], childrens: [Individual]) -> [Individual]:
        """
        Оператор мутации (изменение параметра особи с некоторой заданной вероятностью)
        :param population: список особей
        :param childrens: список детей
        :return: список особей-мутантов
        """
        mutants = []
        p1 = GV.PARAMETERS.mutation_probability * 100
        p2 = 100 - p1
        for child in childrens:
            new_code = ''
            for c in list(child.code):
                new_c = None
                if c == '1':
                    new_code += random.choices(['0', '1'], weights=[p1, p2], k=1)[0]
                else:
                    new_code += random.choices(['0', '1'], weights=[p2, p1], k=1)[0]

            # проверка на корректные значения после мутации и дублирование
            if new_code == child.code:
                mutants.append(child)
                continue
            else:
                new_individual = Individual.new_individual_by_code(new_code)
                if DuplicateCheck.individual_addition(population, new_individual):
                    mutants.append(new_individual)
        return mutants
    
    
if __name__ == '__main__':
    pass