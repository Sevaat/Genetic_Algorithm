import math
from typing import Any, Dict, Union

from src.classical_genetic_algorithm.model.individual import Individual


def get_result_objective_function(individual: Individual, parameters: Dict[str, Any]) -> Union[Individual, None]:
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
            function_value = ind_par[0] * math.sin(10 * math.pi * ind_par[0]) + 1  # пример пользовательской функции

            # конец пользовательской функции

            individual.rank = function_value
        except Exception as e:
            print(f"Ошибка: {e}")
            print("Введена некорректная функция или функция принимает некорректные аргументы.")
            print("Проверьте правильность введенной информации и повторите попытку.")

        return individual
    return None
