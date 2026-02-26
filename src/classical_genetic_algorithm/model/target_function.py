import math
from typing import List, Dict, Any

from src.classical_genetic_algorithm.model.individual import Individual


def get_result_user_defined_function(population: List[Individual], parameters: Dict[str, Any]) -> List[Individual]:
    """
    Пользовательская целевая функция (задаётся пользователем)

    :param parameters: параметры ГА
    :param population: список особей

    :return: список особей без некорректных (значение хромосомы выходит за допустимые границы)
    """

    if not population:
        raise KeyError('Список особей пуст')

    new_individuals = []
    for ind in population:
        if ind.overstepping(parameters):
            individual_parameters = ind.transcript_individual(parameters)
            try:
                # начало пользовательской функции (individual_parameters представляет собой список строчных значений)

                function_value = sum([float(p) for p in individual_parameters]) # пример пользовательской функции

                # конец пользовательской функции

                ind.rank = function_value
            except Exception as e:
                print(f"Ошибка: {e}")
                print("Введена некорректная функция или функция принимает некорректные аргументы.")
                print("Проверьте правильность введенной информации и повторите попытку.")
            new_individuals.append(ind)

    return new_individuals

def get_result_objective_function(individual: Individual, parameters: Dict[str, Any]) -> Individual:
    """
    Пользовательская целевая функция (задаётся пользователем)

    :param parameters: параметры ГА
    :param individual: особь

    :return: список особей без некорректных (значение хромосомы выходит за допустимые границы)
    """

    if individual.overstepping(parameters):
        individual_parameters = individual.transcript_individual(parameters)
        try:
            # начало пользовательской функции (individual_parameters представляет собой список строчных значений)

            ind_par = [float(p) for p in individual_parameters]
            function_value = ind_par[0] * math.sin(10 * math.pi * ind_par[0]) + 1 # пример пользовательской функции

            # конец пользовательской функции

            individual.rank = function_value
        except Exception as e:
            print(f"Ошибка: {e}")
            print("Введена некорректная функция или функция принимает некорректные аргументы.")
            print("Проверьте правильность введенной информации и повторите попытку.")
        return individual
