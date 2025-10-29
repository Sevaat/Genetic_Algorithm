import json
import os
from pathlib import Path
from typing import Callable
from src.classical_genetic_algorithm.options.operators import Operators
from src.classical_genetic_algorithm.options.parameters import Parameters


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
        """
        Читать JSON файл
        :return:
        """
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
        """
        Получать операторы и параметры ГА
        :param users_function: пользовательская функция
        :return: операторы, параметры ГА
        """
        data = CGA.__load_data()
        operators = Operators(data["operators"], users_function)
        parameters = Parameters(data["parameters"])
        return operators, parameters

    def run(self):
        """
        Оптимизировать задачи с использованием классического генетического алгоритма
        :return:
        """
        population = self.operators.population_initialization(self.parameters)
        population = self.operators.target_function(population, self.parameters)


        era = 0
        while era < self.parameters.number_of_eras:
            parents = self.operators.parent_selection(population)
            children = self.operators.recombination(population, parents)
            del parents
            mutants = self.operators.mutation(population, children)
            del children
            mutants = self.operators.target_function(mutants)
            population = self.operators.replacement(population, mutants)
            del mutants
            if self.operators.stops(population):
                break
            else:
                era += 1
            return population[:self.parameters.number_of_results]

