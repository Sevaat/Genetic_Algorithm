import pytest

from src.model.classic.classical_genetic_algorithm_parameters import CGAParameters

def test_classical_genetic_algorithm_parameters_valid():
    params = CGAParameters()
    setattr(params, 'number_of_individuals', '10')
    assert getattr(params, 'number_of_individuals') == 10

    setattr(params, 'proportion_of_elite_individuals', '0.5')
    assert getattr(params, 'proportion_of_elite_individuals') == 0.5

    setattr(params, 'number_of_eras', '100')
    assert getattr(params, 'number_of_eras') == 100

    setattr(params, 'mutation_probability', '0.01')
    assert getattr(params, 'mutation_probability') == 0.01

    setattr(params, 'change_counter', '5')
    assert getattr(params, 'change_counter') == 5

    setattr(params, 'number_of_results', '3')
    assert getattr(params, 'number_of_results') == 3

    setattr(params, 'recombination_point_count', '2')
    assert getattr(params, 'recombination_point_count') == 2

    setattr(params, 'number_of_recurring_individuals', '4')
    assert getattr(params, 'number_of_recurring_individuals') == 4

    data = ['1 2', '3 4']
    params.gene_sets = data
    assert params.gene_sets == [['1', '2'], ['3', '4']]

    data = ['1 2', 'd 3 5 1']
    params.gene_sets = data
    assert params.gene_sets == [['1', '2'], ['3.0', '4.0', '5.0']]

def test_classical_genetic_algorithm_parameters_invalid_value():
    params = CGAParameters()
    with pytest.raises(ValueError):
        setattr(params, 'number_of_individuals', '-1')

    with pytest.raises(ValueError):
        setattr(params, 'proportion_of_elite_individuals', '1.5')

    with pytest.raises(ValueError):
        setattr(params, 'number_of_eras', '-10')

    with pytest.raises(ValueError):
        setattr(params, 'mutation_probability', '-0.5')

    with pytest.raises(ValueError):
        setattr(params, 'change_counter', '-2')

    with pytest.raises(ValueError):
        setattr(params, 'number_of_results', '-3')

    with pytest.raises(ValueError):
        setattr(params, 'recombination_point_count', '-2')

    with pytest.raises(ValueError):
        setattr(params, 'number_of_recurring_individuals', '-4')

def test_classical_genetic_algorithm_parameters_invalid_type():
    params = CGAParameters()
    with pytest.raises(TypeError):
        setattr(params, 'number_of_individuals', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'proportion_of_elite_individuals', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'number_of_eras', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'mutation_probability', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'change_counter', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'number_of_results', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'recombination_point_count', 'abc')

    with pytest.raises(TypeError):
        setattr(params, 'number_of_recurring_individuals', 'abc')