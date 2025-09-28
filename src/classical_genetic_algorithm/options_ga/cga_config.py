from typing import Callable

from src.classical_genetic_algorithm.options_ga.cga_parameters import get_parameters
from src.classical_genetic_algorithm.options_ga.cga_settings import get_settings


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
        self.__settings = get_settings(settings, function)
        self.__parameters = get_parameters(parameters)

    @property
    def settings(self):
        return self.__settings

    @property
    def parameters(self):
        return self.__parameters