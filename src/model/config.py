from typing import Callable

from src.model.classic.classical_genetic_algorithm_parameters import CGAParameters
from src.model.classic.classical_genetic_algorithm_settings import CGASettingsReplacementBuilder


def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singleton
class Config:
    def __init__(self, settings: dict, parameters: dict, function: Callable):
        settings_builder = CGASettingsReplacementBuilder()
        ga_settings = settings_builder.\
            parent_selection(settings['parent_selection']). \
            stops(settings['stops']). \
            purpose(settings['purpose']). \
            recombination(settings['recombination']). \
            target_function(function). \
            population_initialization(settings['population_initialization']). \
            mutation(settings['mutation']). \
            replacement(settings['replacement']). \
            build()

        ga_parameters = CGAParameters()
        ga_parameters.number_of_individuals = parameters['number_of_individuals']
        ga_parameters.proportion_of_elite_individuals = parameters['proportion_of_elite_individuals']
        ga_parameters.number_of_eras = parameters['number_of_eras']
        ga_parameters.gene_sets = parameters['gene_sets']
        ga_parameters.mutation_probability = parameters['mutation_probability']
        ga_parameters.change_counter = parameters['change_counter']
        ga_parameters.number_of_results = parameters['number_of_results']
        ga_parameters.recombination_point_count = parameters['recombination_point_count']
        ga_parameters.number_of_recurring_individuals = parameters['number_of_recurring_individuals']

        self.__settings = ga_settings
        self.__parameters = ga_parameters

    @property
    def settings(self):
        return self.__settings

    @property
    def parameters(self):
        return self.__parameters