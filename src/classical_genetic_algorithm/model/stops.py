from abc import ABC
from typing import Union, List, Dict, Any

from src.classical_genetic_algorithm.model.individual import Individual
from src.classical_genetic_algorithm.options.parameters import Parameters


class Stops(ABC):
    @staticmethod
    def stopping_for_the_best(stops_dict: Dict[str, Any]) -> bool:
        """
        Проверка на неизменность лучшей особи на протяжении ряда эпох

        Ожидаемое содержание словаря:
        individuals: List[Individual], best_individual: Union[Individual, None], counter: int, parameters: Parameters

        :param stops_dict: список отсортированных особей, лучшая особь, количество повторений лучшей особи, параметры ГА
        :return: вывод True, если на протяжении ряда эпох не было изменения лучшей особи
        """
        if stops_dict['best_individual'] is None:
            stops_dict['best_individual'] = stops_dict['individuals'][0]
            stops_dict['counter'] = stops_dict['parameters'].change_counter
        elif stops_dict['individuals'][0] == stops_dict['best_individual']:
            stops_dict['counter'] -= 1
            return stops_dict['counter'] == 0
        else:
            stops_dict['counter'] = stops_dict['parameters'].change_counter
            stops_dict['best_individual'] = stops_dict['individuals'][0]
        return False

    @staticmethod
    def stopping_by_the_number_of_eras(stops_dict) -> bool:
        """
        Останов по количеству эпох

        Ожидаемое содержание словаря:
        era: int, parameters: Parameters

        :param stops_dict: номер текущей эры, параметры ГА
        :return: вывод False
        """
        if stops_dict['era'] == stops_dict['parameters'].number_of_eras:
            return True
        else:
            stops_dict['era'] += 1
        return False
