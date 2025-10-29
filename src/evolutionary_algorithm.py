from abc import ABC
from typing import Callable

from src.classical_genetic_algorithm.utils.cga_file_manager import FileManager

# class EvolutionaryAlgorithm(ABC):
#     @staticmethod
#     def classical_genetic_algorithm(user_function: Callable, filepath: str = ''):
#         """
#         Оптимизация с использованием классического генетического алгоритма
#         :param user_function: целевая функция, с помощью которой оцениваются решения
#         :param filepath: путь к файлу с исходными данными
#         :return: None
#         """
#         setting, parameters = FileManager.open_file(filepath)
#         from src.classical_genetic_algorithm.options.cga_config import Config
#         Config(setting, parameters, user_function)
#         del setting, parameters
#         result = start()
#         FileManager.save_file(result)