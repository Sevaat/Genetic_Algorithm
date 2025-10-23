from typing import Callable

from src.classical_genetic_algorithm.model.cga_population_initialization import Population
from src.classical_genetic_algorithm.utils.cga_purpose import Purpose
from src.classical_genetic_algorithm.model.cga_recombination import Recombination
from src.classical_genetic_algorithm.model.cga_replacement import Replacement
from src.classical_genetic_algorithm.model.cga_parent_selection import Selection
from src.classical_genetic_algorithm.model.cga_stops import Stops
from src.classical_genetic_algorithm.model.cga_mutation import Mutation
from src.classical_genetic_algorithm.model.cga_target_function import TargetFunction

class Operators:
    """
    Настройки классического генетического алгоритма
    """
    def __init__(self):
        self._parent_selection = None               # тип выбора родителей
        self._stops = None                          # условия останова
        self._purpose = None                        # цель оптимизации (min, max)
        self._recombination = None                  # тип рекомбинации
        self._target_function = None                # целевая функция
        self._population_initialization = None      # способ инициализации новой популяции
        self._mutation = None                       # тип мутации
        self._replacement = None                    # тип замены популяции

    @property
    def parent_selection(self):
        return self._parent_selection

    @parent_selection.setter
    def parent_selection(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._parent_selection = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def stops(self):
        return self._stops

    @stops.setter
    def stops(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._stops = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._purpose = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def recombination(self):
        return self._recombination

    @recombination.setter
    def recombination(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._recombination = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def target_function(self):
        return self._target_function

    @target_function.setter
    def target_function(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._target_function = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def population_initialization(self):
        return self._population_initialization

    @population_initialization.setter
    def population_initialization(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._population_initialization = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def mutation(self):
        return self._mutation

    @mutation.setter
    def mutation(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._mutation = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def replacement(self):
        return self._replacement

    @replacement.setter
    def replacement(self, value: Callable):
        if value is None:
            raise TypeError('Значение None не может быть оператором.')
        if isinstance(value, Callable):
            self._replacement = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

# строитель через наследование
class OperatorsBuilder:
    """
    Родительский класс строителя
    """
    def __init__(self):
        self.settings = Operators()

    def build(self):
        return self.settings

class OperatorsParentSelectionBuilder(OperatorsBuilder):
    """
    Выбор родителей
    """
    def parent_selection(self, selection):
        if selection == 'standard':
            self.settings.parent_selection = Selection.standard_selection
        elif selection == 'stochastic universal sampling':
            self.settings.parent_selection = Selection.stochastic_universal_sampling
        else:
            self.settings.parent_selection = None
        return self

class OperatorsStopsBuilder(OperatorsParentSelectionBuilder):
    """
    Условия останова
    """
    def stops(self, stops):
        if stops == 'epochs':
            self.settings.stops = Stops.stopping_by_the_number_of_eras
        elif stops == 'immutability':
            self.settings.stops = Stops.stopping_for_the_best
        else:
            self.settings.stops = None
        return self

class OperatorsPurposeBuilder(OperatorsStopsBuilder):
    """
    Направление оптимизации
    """
    def purpose(self, purpose):
        if purpose == 'minimum':
            self.settings.purpose = Purpose.sort_by_more
        elif purpose == 'maximum':
            self.settings.purpose = Purpose.sort_by_less
        else:
            self.settings.purpose = None
        return self

class OperatorsRecombinationBuilder(OperatorsPurposeBuilder):
    """
    Вид рекомбинации параметров особи
    """
    def recombination(self, recombination):
        if recombination == 'point':
            self.settings.recombination = Recombination.point_crossing
        elif recombination == 'segmented':
            self.settings.recombination = Recombination.segmental_crossing
        elif recombination == 'uniform':
            self.settings.recombination = Recombination.even_crossing
        else:
            self.settings.recombination = None
        return self

class OperatorsTargetFunctionBuilder(OperatorsRecombinationBuilder):
    """
    Расчет целевой функции
    """
    def target_function(self, user_function):
        if not isinstance(user_function, Callable):
            raise TypeError('На вход должна приходить функция')
        TargetFunction._function = user_function
        self.settings.target_function = TargetFunction.get_result_user_defined_function
        return self

class OperatorsPopulationInitializationBuilder(OperatorsTargetFunctionBuilder):
    """
    Инициализация начальной популяции
    """
    def population_initialization(self, initialization):
        if initialization == 'random':
            self.settings.population_initialization = Population.get_new_random_population
        else:
            self.settings.population_initialization = None
        return self

class OperatorsMutationInitializationBuilder(OperatorsPopulationInitializationBuilder):
    """
    Тип мутации особи
    """
    def mutation(self, mutation):
        if mutation == 'simple mutation':
            self.settings.mutation = Mutation.mutation
        else:
            self.settings.mutation = None
        return self

class OperatorsReplacementBuilder(OperatorsMutationInitializationBuilder):
    """
    Тип отбора лучших особей
    """
    def replacement(self, replacement):
        if replacement == 'elite':
            self.settings.replacement = Replacement.elite
        elif replacement == 'easy cut':
            self.settings.replacement = Replacement.simple_cut
        else:
            self.settings.replacement = None
        return self

def get_operators(data_operators: dict, users_function: Callable):
    """
    Получить набор актуальных операторов для ГА
    :param data_operators: список данных операторов пользователя
    :param users_function: пользовательская целевая функция
    :return: набор актуальных операторов ГА (используемых в рамках данной задача)
    """
    operators_builder = OperatorsReplacementBuilder()
    operators = operators_builder. \
        parent_selection(data_operators["parent selection"]). \
        stops(data_operators["stops"]). \
        purpose(data_operators["purpose"]). \
        recombination(data_operators["recombination"]). \
        target_function(users_function). \
        population_initialization(data_operators["population initialization"]). \
        mutation(data_operators["simple mutation"]). \
        replacement(data_operators["elite"]). \
        build()
    return operators