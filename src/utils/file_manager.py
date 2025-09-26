import os
from pathlib import Path
from abc import ABC
from datetime import datetime
from typing import List, Tuple
from src.model.IndividualClass import Individual
from src.model.classic.classical_genetic_algorithm_parameters import CGAParameters
from src.model.classic.classical_genetic_algorithm_settings import CGASettings


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
            filepath = Path(__file__).resolve().parent.parent / "Data"
            os.makedirs(filepath, exist_ok=True)
            filepath = f"{filepath}/results_{date}.txt"
            with open(filepath, "w", encoding="utf-8") as file:
                for res in result:
                    file.write(f'{res}\n')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def open_file(filepath: str) -> Tuple[dict, dict]:
        """
        Открывать файлы с исходными настройками генетического алгоритма
        :param filepath: путь к файлу с исходными данными генетического алгоритма
        :return:
        """
        if filepath == '':
            filepath = Path(__file__).resolve().parent.parent / "Data"
            os.makedirs(filepath, exist_ok=True)
            filepath = f"{filepath}/input_data.txt"
        try:
            settings = {}
            parameters = {}
            n_settings = vars(CGASettings()).keys()
            n_parameters = vars(CGAParameters()).keys()
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(':')
                    if data[0] in n_settings:
                        settings[data[0]] = data[1].strip()
                    elif data[0] in n_parameters and data[0] != 'gene_sets':
                        parameters[data[0]] = data[1].strip()
                    elif data[0] in n_parameters and data[0] == 'gene_sets' and data[0] not in parameters.keys():
                        parameters[data[0]] = [data[1].strip()]
                    elif data[0] in n_parameters and data[0] == 'gene_sets' and data[0] in parameters.keys():
                        parameters[data[0]].append(data[1].strip())
                    else:
                        continue
            if len(settings) != len(n_settings) - 1 or len(parameters) != len(parameters):
                raise ValueError(
                    'Не все данные для работы алгоритма были получены.\nПроверьте файл загрузки и документацию.')
            return settings, parameters
        except Exception as e:
            print(f'Ошибка: {e}')
