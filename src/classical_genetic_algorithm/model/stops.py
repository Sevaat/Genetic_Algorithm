from abc import ABC
from typing import Dict, Any


class Stops(ABC):
    @staticmethod
    def stopping_for_the_best(**kwargs) -> bool:
        """
        Проверка на неизменность лучшей особи на протяжении ряда эпох

        Ожидаемое содержание словаря:
        individuals: List[Individual], best_individual: Union[Individual, None], counter: int, parameters: Parameters

        :param kwargs: список отсортированных особей, лучшая особь, количество повторений лучшей особи, параметры ГА
        :return: вывод True, если на протяжении ряда эпох не было изменения лучшей особи
        """
        if kwargs['best_individual'] is None:
            kwargs['best_individual'] = kwargs['individuals'][0]
            kwargs['counter'] = kwargs['parameters'].change_counter
        elif kwargs['individuals'][0] == kwargs['best_individual']:
            kwargs['counter'] -= 1
            return kwargs['counter'] == 0
        else:
            kwargs['counter'] = kwargs['parameters'].change_counter
            kwargs['best_individual'] = kwargs['individuals'][0]
        return False

    @staticmethod
    def stopping_by_the_number_of_eras(**kwargs) -> bool:
        """
        Останов по количеству эпох

        Ожидаемое содержание словаря:
        era: int, parameters: Parameters

        :param kwargs: номер текущей эры, параметры ГА
        :return: вывод False
        """
        if kwargs['era'] == kwargs['parameters'].number_of_eras:
            return True
        else:
            kwargs['era'] += 1
        return False

    @staticmethod
    def stop_for_homogeneity(**kwargs) -> bool:
        """
        Останов по однородности популяции

        Ожидаемое содержание словаря:
        individuals: List[Individual]

        :param kwargs: список отсортированных особей
        :return:
        """
        if kwargs['individuals'].count(kwargs['individuals'][0]) / len(kwargs['individuals']) >= 0.95:
            return True
        return False
