import os
from pathlib import Path
from abc import ABC
from datetime import datetime
from typing import List, Tuple, Union
from src.classical_genetic_algorithm.model.cga_individual import Individual


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
            filepath = f"{filepath}/results_cga_{date}.txt"
            with open(filepath, "w", encoding="utf-8") as file:
                for res in result:
                    file.write(f'{res}\n')
        except Exception as e:
            print(f'Ошибка: {e}')
