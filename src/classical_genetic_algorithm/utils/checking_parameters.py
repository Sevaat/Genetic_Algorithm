from typing import Any


def checking_number_of_individuals(value: Any) -> None:
    """Проверка числа особей в популяции"""

    if not isinstance(value, int):
        raise TypeError("Число особей должно быть целым числом")
    if not (10 <= value <= 1000000):
        raise TypeError("Число особей должно быть в интервале [10; 1000000]")


def checking_proportion_of_elite_individuals(value: Any) -> None:
    """Проверка доли элитных особей"""

    if not isinstance(value, float):
        raise TypeError("Доля элитных особей должно быть рациональным числом")
    if not (0 <= value <= 1):
        raise TypeError("Доля элитных особей должно быть в интервале [0; 1]")


def checking_number_of_eras(value: Any) -> None:
    """Проверка числа поколений"""

    if not isinstance(value, int):
        raise TypeError("Число поколений должно быть целым числом")
    if not (10 <= value <= 1000000):
        raise TypeError("Число поколений должно быть в интервале [10; 1000000]")


def checking_mutation_probability(value: Any) -> None:
    """Проверка вероятности мутации"""

    if not isinstance(value, float):
        raise TypeError("Вероятность мутации должна быть рациональным числом")
    if not (0 <= value <= 1):
        raise TypeError("Вероятность мутации должна быть в интервале [0; 1]")


def checking_change_counter(value: Any) -> None:
    """Проверка количества повторений лучшей особи в ряду последовательных поколений"""

    if not isinstance(value, int):
        raise TypeError("Число повторений должно быть целым числом")
    if not (10 <= value <= 1000000):
        raise TypeError("Число повторений должно быть в интервале [10; 1000000]")


def checking_number_of_results(value: Any) -> None:
    """Проверка количества выводимых результатов"""

    if not isinstance(value, int):
        raise TypeError("Количество выводимых результатов должно быть целым числом")
    if not (1 <= value <= 10):
        raise TypeError("Количество выводимых результатов должно быть в интервале [1; 10]")


def checking_recombination_point_count(value: Any) -> None:
    """Проверка количества точек рекомбинации"""

    if not isinstance(value, int):
        raise TypeError("Количество точек рекомбинации должно быть целым числом")
    if not (1 <= value <= 5):
        raise TypeError("Количество точек рекомбинации должно быть в интервале [1; 5]")


def checking_number_of_recurring_individuals(value: Any) -> None:
    """Проверка количества дубликатов в поколении"""

    if not isinstance(value, int):
        raise TypeError("Количество дубликатов в поколении должно быть целым числом")
    if not (0 <= value <= 5):
        raise TypeError("Количество дубликатов в поколении должно быть в интервале [1; 5]")


def checking_parameters(parameter_name: str, value: Any) -> None:
    """Проверка параметров ГА на корректность"""

    if parameter_name == "number_of_individuals":
        checking_number_of_individuals(value)
    if parameter_name == "proportion_of_elite_individuals":
        checking_proportion_of_elite_individuals(value)
    if parameter_name == "number_of_eras":
        checking_number_of_eras(value)
    if parameter_name == "mutation_probability":
        checking_mutation_probability(value)
    if parameter_name == "change_counter":
        checking_change_counter(value)
    if parameter_name == "number_of_results":
        checking_number_of_results(value)
    if parameter_name == "recombination_point_count":
        checking_recombination_point_count(value)
    if parameter_name == "number_of_recurring_individuals":
        checking_number_of_recurring_individuals(value)
