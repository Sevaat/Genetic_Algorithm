from typing import Callable

from src.model.config import Config
from src.utils.file_manager import FileManager
from src.GeneticAlgorithm import genetic_algorithm


def main_ga(user_function: Callable):
    setting, parameters = FileManager.open_file()
    config = Config(setting, parameters, user_function)
    del setting, parameters
    result = genetic_algorithm()
    FileManager.save_file(result)