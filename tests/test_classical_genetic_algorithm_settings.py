import pytest

from src.calculations.MutationClass import Mutation
from src.model.classic.classical_genetic_algorithm_settings import CGASettingsReplacementBuilder
from src.variation_modules.PopulationClass import Population
from src.variation_modules.PurposeClass import Purpose
from src.variation_modules.RecombinationClass import Recombination
from src.variation_modules.ReplacementClass import Replacement
from src.variation_modules.SelectionClass import Selection
from src.variation_modules.StopsClass import Stops


def test_classical_genetic_algorithm_settings_valid():
    def my_func():
        pass
    settings = {
        'parent_selection': 'СТАНДАРНЫЙ',
        'stops': 'КОЛИЧЕСТВО ЭПОХ',
        'purpose': 'МИНИМУМ',
        'recombination': 'ТОЧЕЧНАЯ',
        'population_initialization': 'СЛУЧАЙНАЯ ГЕНЕРАЦИЯ',
        'mutation': 'ПРОСТАЯ МУТАЦИЯ',
        'replacement': 'ЭЛИТА'
    }

    settings_builder = CGASettingsReplacementBuilder()
    ga_settings = settings_builder. \
        parent_selection(settings['parent_selection']). \
        stops(settings['stops']). \
        purpose(settings['purpose']). \
        recombination(settings['recombination']). \
        population_initialization(settings['population_initialization']). \
        mutation(settings['mutation']). \
        replacement(settings['replacement']). \
        build()
    ga_settings.target_function = my_func


    assert ga_settings.parent_selection == Selection.standart_selection
    assert ga_settings.stops == Stops.stopping_by_the_number_of_eras
    assert ga_settings.purpose == Purpose.sort_by_more
    assert ga_settings.recombination == Recombination.point_crossing
    assert ga_settings.target_function == my_func
    assert ga_settings.population_initialization == Population.get_new_random_population
    assert ga_settings.mutation == Mutation.mutation
    assert ga_settings.replacement == Replacement.elite

    settings = {
        'parent_selection': 'СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА',
        'stops': 'НЕИЗМЕНЯЕМОСТЬ',
        'purpose': 'МАКСИМУМ',
        'recombination': 'СЕГМЕНТИРОВАННАЯ',
        'population_initialization': 'СЛУЧАЙНАЯ ГЕНЕРАЦИЯ',
        'mutation': 'ПРОСТАЯ МУТАЦИЯ',
        'replacement': 'ПРОСТОЙ СРЕЗ'
    }

    settings_builder = CGASettingsReplacementBuilder()
    ga_settings = settings_builder. \
        parent_selection(settings['parent_selection']). \
        stops(settings['stops']). \
        purpose(settings['purpose']). \
        recombination(settings['recombination']). \
        population_initialization(settings['population_initialization']). \
        mutation(settings['mutation']). \
        replacement(settings['replacement']). \
        build()
    ga_settings.target_function = my_func

    assert ga_settings.parent_selection == Selection.stochastic_universal_sampling
    assert ga_settings.stops == Stops.stopping_for_the_best
    assert ga_settings.purpose == Purpose.sort_by_less
    assert ga_settings.recombination == Recombination.segmental_crossing
    assert ga_settings.target_function == my_func
    assert ga_settings.population_initialization == Population.get_new_random_population
    assert ga_settings.mutation == Mutation.mutation
    assert ga_settings.replacement == Replacement.simple_cut

    settings = {
        'parent_selection': 'СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА',
        'stops': 'НЕИЗМЕНЯЕМОСТЬ',
        'purpose': 'МАКСИМУМ',
        'recombination': 'РАВНОМЕРНАЯ',
        'population_initialization': 'СЛУЧАЙНАЯ ГЕНЕРАЦИЯ',
        'mutation': 'ПРОСТАЯ МУТАЦИЯ',
        'replacement': 'ПРОСТОЙ СРЕЗ'
    }

    settings_builder = CGASettingsReplacementBuilder()
    ga_settings = settings_builder. \
        parent_selection(settings['parent_selection']). \
        stops(settings['stops']). \
        purpose(settings['purpose']). \
        recombination(settings['recombination']). \
        population_initialization(settings['population_initialization']). \
        mutation(settings['mutation']). \
        replacement(settings['replacement']). \
        build()
    ga_settings.target_function = my_func

    assert ga_settings.parent_selection == Selection.stochastic_universal_sampling
    assert ga_settings.stops == Stops.stopping_for_the_best
    assert ga_settings.purpose == Purpose.sort_by_less
    assert ga_settings.recombination == Recombination.even_crossing
    assert ga_settings.target_function == my_func
    assert ga_settings.population_initialization == Population.get_new_random_population
    assert ga_settings.mutation == Mutation.mutation
    assert ga_settings.replacement == Replacement.simple_cut

def test_classical_genetic_algorithm_settings_invalid():
    def my_func():
        pass
    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('ПРОВЕРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('МАКСИМУМ'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('ПРОВЕРКА'). \
            purpose('МАКСИМУМ'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('ПРОВЕРКА'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('МАКСИМУМ'). \
            recombination('ПРОВЕРКА'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('МАКСИМУМ'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('ПРОВЕРКА'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('МАКСИМУМ'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОВЕРКА'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('МАКСИМУМ'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОВЕРКА'). \
            build()
        ga_settings.target_function = my_func

    with pytest.raises(TypeError):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder. \
            parent_selection('СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА'). \
            stops('НЕИЗМЕНЯЕМОСТЬ'). \
            purpose('МАКСИМУМ'). \
            recombination('РАВНОМЕРНАЯ'). \
            population_initialization('СЛУЧАЙНАЯ ГЕНЕРАЦИЯ'). \
            mutation('ПРОСТАЯ МУТАЦИЯ'). \
            replacement('ПРОСТОЙ СРЕЗ'). \
            build()
        ga_settings.target_function = 'ПРОВЕРКА'