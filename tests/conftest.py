import copy
from typing import List

import pytest


@pytest.fixture
def cga_parameters():
    parameters = {
        'number_of_individuals': 10,
        'proportion_of_elite_individuals': 0.5,
        'number_of_eras': 10,
        'mutation_probability': 0.01,
        'change_counter': 5,
        'number_of_results': 3,
        'recombination_point_count': 1,
        'number_of_recurring_individuals': 1,
        'gene_sets': ['1 2 3', '4 5 6', '7 8 9']
    }
    return parameters

@pytest.fixture
def cga_settings():
    settings = {
        'parent_selection': 'СТАНДАРНЫЙ',
        'stops': 'КОЛИЧЕСТВО ЭПОХ',
        'purpose': 'МИНИМУМ',
        'recombination': 'ТОЧЕЧНАЯ',
        'population_initialization': 'СЛУЧАЙНАЯ ГЕНЕРАЦИЯ',
        'mutation': 'ПРОСТАЯ МУТАЦИЯ',
        'replacement': 'ЭЛИТА'
    }
    def target_function(individual_parameters: List[str]):
        return sum(int(ip) for ip in individual_parameters)
    return settings, target_function

@pytest.fixture
def cga_config(cga_parameters, cga_settings):
    from src.classical_genetic_algorithm.options_ga.cga_config import Config
    config = Config(cga_settings[0], cga_parameters, cga_settings[1])
    return config

@pytest.fixture
def cga_population(cga_config):
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    individual0 = Individual.new_individual_by_code('001100') # ['1', '6', '7']
    individual1 = Individual.new_individual_by_code('010001') # ['2', '4', '8']
    individual2 = Individual.new_individual_by_code('010111') # ['2', '5', '9']
    individual3 = Individual.new_individual_by_code('010000') # ['2', '4', '7']
    individual4 = Individual.new_individual_by_code('011100') # ['2', '6', '7']
    individual5 = Individual.new_individual_by_code('110101') # ['3', '5', '8']
    individual6 = Individual.new_individual_by_code('110011') # ['3', '4', '9']
    individual7 = Individual.new_individual_by_code('000100') # ['1', '5', '7']
    individual8 = Individual.new_individual_by_code('000011') # ['1', '4', '9']
    individual9 = Individual.new_individual_by_code('110001') # ['3', '4', '8']
    return [individual0, individual1, individual2, individual3, individual4,
            individual5, individual6, individual7, individual8, individual9]

@pytest.fixture
def cga_population_with_tf(cga_population):
    population = copy.deepcopy(cga_population)
    population[0].rank = 14
    population[1].rank = 14
    population[2].rank = 16
    population[3].rank = 13
    population[4].rank = 15
    population[5].rank = 16
    population[6].rank = 16
    population[7].rank = 13
    population[8].rank = 14
    population[9].rank = 15
    return population

@pytest.fixture
def cga_parents(cga_population_with_tf):
    parents = [
        (cga_population_with_tf[0], cga_population_with_tf[1]),
        (cga_population_with_tf[0], cga_population_with_tf[2]),
        (cga_population_with_tf[0], cga_population_with_tf[3]),
        (cga_population_with_tf[0], cga_population_with_tf[4]),
        (cga_population_with_tf[0], cga_population_with_tf[5]),
        (cga_population_with_tf[0], cga_population_with_tf[6]),
        (cga_population_with_tf[0], cga_population_with_tf[7]),
        (cga_population_with_tf[0], cga_population_with_tf[8]),
        (cga_population_with_tf[0], cga_population_with_tf[9]),
        (cga_population_with_tf[1], cga_population_with_tf[2])
    ]
    return parents

@pytest.fixture
def cga_children(cga_config):
    from src.classical_genetic_algorithm.model.cga_individual import Individual
    children = [
        Individual().new_individual_by_code('000001'),
        Individual().new_individual_by_code('010100'),
        Individual().new_individual_by_code('001101'),
        Individual().new_individual_by_code('110100'),
        Individual().new_individual_by_code('001111'),
        Individual().new_individual_by_code('110000'),
        Individual().new_individual_by_code('001111'),
        Individual().new_individual_by_code('000000'),
        Individual().new_individual_by_code('000001'),
        Individual().new_individual_by_code('111100'),
    ]
    return children
