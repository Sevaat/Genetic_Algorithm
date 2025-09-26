from abc import ABC
from typing import Callable

from src.model.config import Config
from src.utils.file_manager import FileManager
from src.GeneticAlgorithm import genetic_algorithm

class EvolutionaryAlgorithm(ABC):
    @staticmethod
    def classical_genetic_algorithm(user_function: Callable, filepath: str = ''):
        """
        Оптимизация с использованием классического генетического алгоритма
        :param user_function: целевая функция, с помощью которой оцениваются решения
        :param filepath: путь к файлу с исходными данными
        :return: None
        """
        setting, parameters = FileManager.open_file(filepath)
        config = Config(setting, parameters, user_function)
        del setting, parameters
        result = genetic_algorithm()
        FileManager.save_file(result)