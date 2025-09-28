from abc import ABC
from src.classical_genetic_algorithm.model.cga_individual import Individual


class TargetFunction(ABC):
    @staticmethod
    def get_result_user_defined_function(individuals: [Individual]) -> [Individual]:
        """
        Пользовательская целевая функция
        :param individuals: список особей
        :return: список особей без некорректных (значение хромосомы выходит за допустимые границы)
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        new_individuals = []
        for ind in individuals:
            if ind.overstepping():
                individual_parameters = ind.transcript_individual()
                try:
                    ind.rank = config.settings.target_function(individual_parameters)
                except Exception as e:
                    print(f'Ошибка: {e}')
                    print('Введена некорректная функция или функция принимает некорректные аргументы.')
                    print('Проверьте правильность введенной информации и повторите попытку.')
                new_individuals.append(ind)
        return new_individuals
