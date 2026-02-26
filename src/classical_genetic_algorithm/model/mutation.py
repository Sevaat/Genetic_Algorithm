import random
from abc import ABC
from typing import List, Dict, Any, Callable

from src.classical_genetic_algorithm.model.individual import Individual
from src.classical_genetic_algorithm.utils.duplicate_check import DuplicateCheck


def inversion_one_bit(
    population: List[Individual], children: List[Individual], parameters: Dict[str, Any]
) -> List[Individual]:
    """
    Оператор мутации (изменение параметра особи с некоторой заданной вероятностью)

    :param parameters: параметры ГА
    :param population: список особей
    :param children: список детей

    :return: список особей-мутантов
    """

    if not population:
        raise KeyError('Список особей пуст')

    if not children:
        raise KeyError('Список детей пуст')

    mutants: List[Individual] = []
    p1 = parameters['mutation_probability'] * 100
    p2 = 100 - p1
    for child in children:
        code_list = []
        for c in list(child.code):
            if c == "1":
                code_list.append(random.choices(["0", "1"], weights=[p1, p2], k=1)[0])
            else:
                code_list.append(random.choices(["0", "1"], weights=[p2, p1], k=1)[0])
        new_code = "".join(code_list)

        # проверка на корректные значения и дублирование после мутации
        new_individual = Individual.new_individual_by_code(new_code, parameters)
        if new_individual is not None:
            if DuplicateCheck.individual_addition(population + mutants, new_individual, parameters):
                mutants.append(new_individual)

    return mutants

def inversion_group_bits(
    population: List[Individual], children: List[Individual], parameters: Dict[str, Any]
) -> List[Individual]:
    """
    Инверсия группы бит - инвертируется несколько подряд идущих генов

    :param parameters: параметры ГА
    :param population: список особей
    :param children: список детей

    :return: список особей-мутантов
    """

    if not population:
        raise KeyError('Список особей пуст')

    if not children:
        raise KeyError('Список детей пуст')

    mutants: List[Individual] = []
    code_length = len(children[0].code)
    for child in children:
        code_list = list(child.code)
        if random.random() < parameters['mutation_probability']:
            start = random.randint(0, code_length - 1)
            end = random.randint(start, code_length - 1)
            for i in range(start, end + 1):
                code_list[i] = "0" if code_list[i] == "1" else "1"
        new_code = "".join(code_list)

        # проверка на корректные значения и дублирование после мутации
        new_individual = Individual.new_individual_by_code(new_code, parameters)
        if new_individual is not None:
            if DuplicateCheck.individual_addition(population + mutants, new_individual, parameters):
                mutants.append(new_individual)

    return mutants

def swap(population: List[Individual], children: List[Individual], parameters: Dict[str, Any]) -> List[Individual]:
    """
    Обмен - два случайно выбранных гена меняются местами

    :param parameters: параметры ГА
    :param population: список особей
    :param children: список детей

    :return: список особей-мутантов
    """

    if not population:
        raise KeyError('Список особей пуст')

    if not children:
        raise KeyError('Список детей пуст')

    mutants: List[Individual] = []
    code_length = len(children[0].code)
    for child in children:
        code_list = list(child.code)
        if random.random() < parameters['mutation_probability'] and code_length > 1:
            point_1, point_2 = random.sample(range(code_length), 2)
            code_list[point_1], code_list[point_2] = code_list[point_2], code_list[point_1]
        new_code = "".join(code_list)

        # проверка на корректные значения и дублирование после мутации
        new_individual = Individual.new_individual_by_code(new_code, parameters)
        if new_individual is not None:
            if DuplicateCheck.individual_addition(population + mutants, new_individual, parameters):
                mutants.append(new_individual)

    return mutants

def reverse(population: List[Individual], children: List[Individual], parameters: Dict[str, Any]) -> List[Individual]:
    """
    Обращение - случайная последовательность генов записывается в обратном порядке

    :param parameters: параметры ГА
    :param population: список особей
    :param children: список детей

    :return: список особей-мутантов
    """

    if not population:
        raise KeyError('Список особей пуст')

    if not children:
        raise KeyError('Список детей пуст')

    mutants: List[Individual] = []
    code_length = len(children[0].code)
    for child in children:
        code_list = list(child.code)
        if random.random() < parameters['mutation_probability'] and code_length > 1:
            start = random.randint(0, code_length - 1)
            end = random.randint(start, code_length - 1)
            code_list[start : end + 1] = code_list[start : end + 1][::-1]
        new_code = "".join(code_list)

        # проверка на корректные значения и дублирование после мутации
        new_individual = Individual.new_individual_by_code(new_code, parameters)
        if new_individual is not None:
            if DuplicateCheck.individual_addition(population + mutants, new_individual, parameters):
                mutants.append(new_individual)

    return mutants

def shuffle(population: List[Individual], children: List[Individual], parameters: Dict[str, Any]) -> List[Individual]:
    """
    Перетасовка - значения выбранной непрерывной последовательности генов перемешиваются случайным образом

    :param parameters: параметры ГА
    :param population: список особей
    :param children: список детей

    :return: список особей-мутантов
    """

    if not population:
        raise KeyError('Список особей пуст')

    if not children:
        raise KeyError('Список детей пуст')

    mutants: List[Individual] = []
    code_length = len(children[0].code) if children else 0
    for child in children:
        code_list = list(child.code)
        if random.random() < parameters['mutation_probability'] and code_length > 1:
            start = random.randint(0, code_length - 1)
            end = random.randint(start, code_length - 1)
            segment = code_list[start : end + 1]
            random.shuffle(segment)
            code_list[start : end + 1] = segment
        new_code = "".join(code_list)

        # проверка на корректные значения и дублирование после мутации
        new_individual = Individual.new_individual_by_code(new_code, parameters)
        if new_individual is not None:
            if DuplicateCheck.individual_addition(population + mutants, new_individual, parameters):
                mutants.append(new_individual)
    return mutants


def get_mutation(data: Dict[str, Any]) -> Callable:
    """Получить метод мутации по исходным данным"""

    if 'mutation' not in data['operators']:
        raise KeyError('В исходных данных отсутствует информация по операторам ГА (operators/mutation)')
    methods = {
        "inversion_one_bit": inversion_one_bit,
        "inversion_group_bits": inversion_group_bits,
        "swap": swap,
        "reverse": reverse,
        "shuffle": shuffle,
    }
    if data['operators']['mutation'] in methods.keys():
        return methods[data['operators']['mutation']]
    else:
        raise KeyError('В исходных данных отсутствует информация по операторам ГА (operators/mutation/method)')
