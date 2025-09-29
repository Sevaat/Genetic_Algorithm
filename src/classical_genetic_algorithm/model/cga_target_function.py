from abc import ABC
from typing import Callable, Union

from src.classical_genetic_algorithm.model.cga_individual import Individual

class TargetFunction(ABC):
    _function: Union[Callable, None] = None

    @staticmethod
    def get_result_user_defined_function(individuals: [Individual]) -> [Individual]:
        """
        Пользовательская целевая функция
        :param individuals: список особей
        :return: список особей без некорректных (значение хромосомы выходит за допустимые границы)
        """
        new_individuals = []
        for ind in individuals:
            if ind.overstepping():
                individual_parameters = ind.transcript_individual()
                try:
                    ind.rank = TargetFunction._function(individual_parameters)
                except Exception as e:
                    print(f'Ошибка: {e}')
                    print('Введена некорректная функция или функция принимает некорректные аргументы.')
                    print('Проверьте правильность введенной информации и повторите попытку.')
                new_individuals.append(ind)
        return new_individuals
