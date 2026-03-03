import json
import multiprocessing
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from classical_genetic_algorithm.model.mutation import get_mutation
from classical_genetic_algorithm.model.parent_selection import get_parent_selection
from classical_genetic_algorithm.model.population_initialization import get_population_initialization
from classical_genetic_algorithm.model.recombination import get_recombination
from classical_genetic_algorithm.model.replacement import get_replacement
from classical_genetic_algorithm.model.stops import get_stops
from classical_genetic_algorithm.model.target_function import get_result_objective_function
from classical_genetic_algorithm.utils.checking_parameters import checking_parameters
from src.classical_genetic_algorithm.model.individual import Individual


class CGA:
    """Класс класического генетического алгоритма"""

    def __init__(self):
        data = CGA._load_data()

        # параметры ГА
        self.parameters = CGA._get_parameters(data)
        self.trend = data["operators"]["purpose"]

        # функции операторов
        self.parent_selection = get_parent_selection(data)
        self.population_initialization = get_population_initialization(data)
        self.target_function = get_result_objective_function
        self.recombination = get_recombination(data)
        self.mutation = get_mutation(data)
        self.replacement = get_replacement(data)
        self.stops = get_stops

    @staticmethod
    def _load_data() -> Dict[str, Any]:
        """
        Читать JSON файл data_cga.json из директории data

        :return: данные классического генетического алгоритма
        """

        filepath = str(Path(__file__).resolve().parent / "data")
        os.makedirs(filepath, exist_ok=True)
        filepath = f"{filepath}/data_cga.json"
        data = {}
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, dict):
                raise TypeError("Исходные данные должны быть словарем")
            print("Файл успешно загружен")
        except FileNotFoundError as e:
            print(f"Файл не найден: {e}")
        except json.JSONDecodeError as e:
            print(f"Ошибка в формате JSON: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        return data

    @staticmethod
    def _get_parameters(data: Dict[str, Any]):
        """Получить параметры ГА из исходных данных"""

        if "parameters" not in data.keys():
            raise KeyError("В исходных данных отсутствует информация по параметрам ГА (parameters)")

        parameters = {
            "number_of_individuals": None,
            "proportion_of_elite_individuals": None,
            "number_of_eras": None,
            "mutation_probability": None,
            "change_counter": None,
            "number_of_results": None,
            "recombination_point_count": None,
            "number_of_recurring_individuals": None,
            "gene_sets": None,
        }

        if not isinstance(data["parameters"], dict):
            raise TypeError("Набор параметров должен быть словарем")
        for key in parameters.keys():
            if key != "gene_sets":
                if key not in data["parameters"].keys():
                    raise KeyError(f"В исходных данных отсутствует информация по параметрам ГА (parameters/{key})")
                else:
                    checking_parameters(key, data["parameters"][key])
                    parameters[key] = data["parameters"][key]

        if "gene_sets" not in data["parameters"].keys():
            raise KeyError("В исходных данных отсутствует информация по параметрам ГА (parameters/gene_sets)")
        else:
            gene_sets = []
            if not isinstance(data["parameters"]["gene_sets"], dict):
                raise TypeError("Набор генов должен быть словарем")
            if "simple_set" in data["parameters"]["gene_sets"].keys():
                if not isinstance(data["parameters"]["gene_sets"]["simple_set"], list):
                    raise TypeError("Данные простого набора генов должны быть списком")
                for gs in data["parameters"]["gene_sets"]["simple_set"]:
                    if not isinstance(gs, str):
                        raise TypeError("Простой набор генов должен быть строкой")
                    gene_sets.append(gs.split())
            if "step_set" in data["parameters"]["gene_sets"].keys():
                if not isinstance(data["parameters"]["gene_sets"]["step_set"], list):
                    raise TypeError("Данные набора генов с шагом должны быть списком")
                for gs in data["parameters"]["gene_sets"]["step_set"]:
                    if not isinstance(gs, dict):
                        raise TypeError("Набор генов с шагом должен быть словарем")
                    gene_set = []
                    if "start" not in gs.keys() or "end" not in gs.keys() or "step" not in gs.keys():
                        raise KeyError(
                            "Словерь набора гена с шагом не содержит обязательного ключа (start, end, step)"
                        )
                    start, end, step = gs["start"], gs["end"], gs["step"]
                    if not isinstance(start, float | int):
                        raise TypeError("Начало последовательности должно быть рациональным (целым) числом")
                    if not isinstance(end, float | int):
                        raise TypeError("Конец последовательности должен быть рациональным (целым) числом")
                    if not isinstance(step, float | int):
                        raise TypeError("Шаг последовательности должен быть рациональным (целым) числом")
                    if start > end or step <= 0:
                        raise ValueError("Проверьте правильность ввода: start <= end; step > 0")
                    while start <= end:
                        gene_set.append(str(start))
                        start += step
                    gene_sets.append(gene_set)
            parameters["gene_sets"] = gene_sets

        return parameters

    @staticmethod
    def _save_data(population: List[Individual], parameters: Dict[str, Any]) -> None:
        """
        Запись в JSON файл result_cga_...,json в директорию result

        :return: None
        """

        filepath = str(Path(__file__).resolve().parent / "result")
        os.makedirs(filepath, exist_ok=True)
        filepath = f"{filepath}/result_cga_{datetime.now().strftime("%d.%m.%Y_%H-%M-%S")}.json"
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump([ind.to_dict(parameters) for ind in population], file)
            print("Запись результатов прошла успешно")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def run(self) -> None:
        """
        Оптимизировать задачи с использованием классического генетического алгоритма

        :return:
        """

        with multiprocessing.Pool() as pool:
            best_individual = None
            counter = self.parameters["change_counter"]

            population = self.population_initialization(self.parameters)

            args = [(individual, self.parameters) for individual in population]
            population = pool.starmap(self.target_function, args)

            era = 0
            while True:
                parents = self.parent_selection(population, self.trend)
                children = self.recombination(population, parents, self.parameters)
                mutants = self.mutation(population, children, self.parameters)

                args = [(individual, self.parameters) for individual in mutants]
                mutants = pool.starmap(self.target_function, args)

                population = self.replacement(population, mutants, self.parameters, self.trend)

                best_individual, counter, stop_1, stop_2, stop_3 = self.stops(
                    population, best_individual, counter, self.trend, era, self.parameters
                )
                if stop_1 or stop_2 or stop_3:
                    if stop_1:
                        print("Останов по причине неизменности особи")
                    if stop_2:
                        print("Останов по причине окончания эр")
                    if stop_3:
                        print("Останов по причине однородности популяции")
                    print(f"Расчет окончен на эре: {era}")
                    break
                else:
                    era += 1
        self._save_data(population[: self.parameters["number_of_results"]], self.parameters)
