from typing import Callable, Union

from src.classical_genetic_algorithm.model.cga_individual import Individual
from src.classical_genetic_algorithm.options_ga.parameters import get_parameters
from src.classical_genetic_algorithm.options_ga.operators import get_operators


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
        self.__settings = get_operators(settings, function)
        self.__parameters = get_parameters(parameters)
        self.__counter = self.__parameters.change_counter
        self.__best_individual = None

    @property
    def settings(self):
        return self.__settings

    @property
    def parameters(self):
        return self.__parameters

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, new_counter):
        if isinstance(new_counter, int):
            self.__counter = new_counter

    @property
    def best_individual(self):
        return self.__best_individual

    @best_individual.setter
    def best_individual(self, new_best_individual):
        if isinstance(new_best_individual, Individual):
            self.__best_individual = new_best_individual
