import json
import os
from pathlib import Path
from typing import Callable
from src.classical_genetic_algorithm.options_ga.operators import get_operators
from src.classical_genetic_algorithm.options_ga.parameters import get_parameters


class CGA:
    def __init__(self, users_function: Callable):
        self.__operators, self.__parameters = CGA.__get_operators_and_parameters(users_function)
        self.__best_individuals = None

    @property
    def parameters(self):
        return self.__parameters

    @property
    def operators(self):
        return self.__operators

    @property
    def best_individuals(self):
        return self.__best_individuals

    @staticmethod
    def __load_data():
        filepath = Path(__file__).resolve().parent / "data"
        os.makedirs(filepath, exist_ok=True)
        filepath = f"{filepath}/data_cga.json"
        data = {}
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            print("Файл успешно загружен")
        except FileNotFoundError as e:
            print(f"Файл не найден: {e}")
        except json.JSONDecodeError as e:
            print(f"Ошибка в формате JSON: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        return data

    @staticmethod
    def __get_operators_and_parameters(users_function: Callable):
        data = CGA.__load_data()

        operators = get_operators(data["operators"], users_function)
        parameters = get_parameters(data["parameters"])

        return operators, parameters

