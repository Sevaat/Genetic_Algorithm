import logging
import os
from pathlib import Path
from tkinter import filedialog
from src.model.genetic_algorithm.GeneticAlgorithmBuilderClass import GeneticAlgorithmBuilder
import src.utils.GlobalVariables as GV
from abc import ABC
from datetime import datetime
from typing import List
from src.model.IndividualClass import Individual
from src.model.genetic_algorithm.GeneticAlgorithmClass import GeneticAlgorithm
from src.model.parameters import Parameters
from src.utils.data_verification import DataVerification

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_dir = Path(__file__).resolve().parent.parent / "logs"
os.makedirs(file_dir, exist_ok=True)
file_handler = logging.FileHandler(filename=f"{file_dir}/file_manager_class.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


class FileManager(ABC):
    @staticmethod
    def save_file(result: List[Individual]) -> None:
        """
        Позволяет сохранять файл в формате txt
        :param result: результат расчета в виде списка лучших особей популяции
        :return: None
        """
        try:
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            filepath = Path(__file__).resolve().parent.parent / "results"
            os.makedirs(filepath, exist_ok=True)
            filepath = f"{filepath}/results_{date}.txt"
            logger.info(f"Путь для сохранения файла: {filepath}")

            with open(filepath, "w", encoding="utf-8") as file:
                for res in result:
                    file.write(f'{res}\n')
            logger.info("Запись в файл прошла успешно")
        except Exception as e:
            logger.error(f"Ошибка: {e}")

    @staticmethod
    def open_file() -> None:
        """
        Открывать файлы с исходными настройками генетического алгоритма
        :return: None
        """
        filepath = filedialog.askopenfilename(
            title='Загрузка файла',
            defaultextension='txt',
            initialfile='Data.txt'
        )
        logger.info(f"Путь для загрузки файла: {filepath}")
        if not filepath:
            logger.warning("Путь для загрузки файла некорректный")

        GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = FileManager.get_parameters(filepath)
        logger.info("Загрузка файла прошла успешно")

    @staticmethod
    def get_genetic_algorithm(filepath: str) -> GeneticAlgorithm:
        """
        Получать настройки генетического алгоритма
        :param filepath: путь к файду с настройками генетического алгоритма
        :return: экземпляр класса генетического алгоритма с настройками
        """
        try:
            logger.info("Начало настройки генетического алгоритма")
            ga = None
            gab = GeneticAlgorithmBuilder()
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(':')
                    if data[0] == 'Тип выбора родителей':
                        ga = gab.parent_selection.set_selection(data[1].strip())
                    elif data[0] == 'Условия останова':
                        ga = gab.stops.set_stops(data[1].strip())
                    elif data[0] == 'Цель оптимизации (min, max)':
                        ga = gab.purpose.set_purpose(data[1].strip())
                    elif data[0] == 'Тип рекомбинации':
                        ga = gab.recombination.set_recombination(data[1].strip())
                    elif data[0] == 'Целевая функция':
                        ga = gab.target_function.set_target_function(data[1].strip())
                    elif data[0] == 'Способ инициализации новой популяции':
                        ga = gab.population_initialization.set_population_initialization(data[1].strip())
                    elif data[0] == 'Замена популяции':
                        ga = gab.replacement.set_replacement(data[1].strip())
                    else:
                        continue
            ga = gab.build()
            logger.info("Настройка генетического алгоритма выполнена успешно")
            return ga
        except Exception as e:
            logger.error(f"Ошибка: {e}")

    @staticmethod
    def get_parameters(filepath: str) -> Parameters:
        """
        Получать параметры генетического алгоритма
        :param filepath: путь к параметрам генетического алгоритма
        :return: экземпляр класса параметров генетического алгоритма
        """
        try:
            logger.info("Начало заполнения параметров генетического алгоритма")
            parameters = Parameters()
            gene_sets = []
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(':')
                    if data[0] == 'Количество особей в популяции':
                        parameters.number_of_individuals = data[1].strip()
                    elif data[0] == 'Доля элитных особей':
                        parameters.proportion_of_elite_individuals = data[1].strip()
                    elif data[0] == 'Количество эпох':
                        parameters.number_of_eras = data[1].strip()
                    elif data[0] == 'Вероятность мутации':
                        parameters.mutation_probability = data[1].strip()
                    elif data[0] == 'Cчетчик изменений лучшей особи':
                        parameters.change_counter = data[1].strip()
                        GV.counter = data[1].strip()
                    elif data[0] == 'Количество выводимых результатов':
                        parameters.number_of_results = data[1].strip()
                    elif data[0] == 'Количество точек рекомбинации':
                        parameters.recombination_point_count = data[1].strip()
                    elif data[0] == 'Ген':
                        gene_sets.append(data[1].strip().split())
                    elif data[0] == 'Ген (н, к, ш)':
                        gene_set = []
                        start, end, step = data[1].strip().split()
                        if DataVerification.is_float(start) and DataVerification.is_float(
                                end) and DataVerification.is_float(step):
                            start, end, step = float(start), float(end), float(step)
                        else:
                            raise TypeError
                        while start <= end:
                            gene_set.append(str(start))
                            start += step
                        gene_sets.append(gene_set)
                    elif data[0] == 'Количество повторяющихся особей':
                        parameters.number_of_recurring_individuals = data[1].strip()
                    else:
                        continue
            parameters.gene_sets = gene_sets
            logger.info("Параметры генетического алгоритма заполнены успешно")
            return parameters
        except Exception as e:
            logger.error(f"Ошибка: {e}")
