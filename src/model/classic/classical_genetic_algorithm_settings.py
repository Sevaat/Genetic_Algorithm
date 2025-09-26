from typing import Callable

from src.calculations.MutationClass import Mutation
from src.variation_modules.PopulationClass import Population
from src.variation_modules.PurposeClass import Purpose
from src.variation_modules.RecombinationClass import Recombination
from src.variation_modules.ReplacementClass import Replacement
from src.variation_modules.SelectionClass import Selection
from src.variation_modules.StopsClass import Stops

settings = None

class CGASettings:
    """
    Настройки классического генетического алгоритма
    """
    def __init__(self):
        self._parent_selection = None # тип выбора родителей
        self._stops = None # условия останова
        self._purpose = None # цель оптимизации (min, max)
        self._recombination = None # тип рекомбинации
        self._target_function = None # целевая функция
        self._population_initialization = None # способ инициализации новой популяции
        self._mutation = None
        self._replacement = None # тип замены популяции

    @property
    def parent_selection(self):
        return self._parent_selection

    @parent_selection.setter
    def parent_selection(self, value: Callable):
        if isinstance(value, Callable):
            self._parent_selection = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def stops(self):
        return self._stops

    @stops.setter
    def stops(self, value: Callable):
        if isinstance(value, Callable):
            self._stops = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value: Callable):
        if isinstance(value, Callable):
            self._purpose = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def recombination(self):
        return self._recombination

    @recombination.setter
    def recombination(self, value: Callable):
        if isinstance(value, Callable):
            self._recombination = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def target_function(self):
        return self._target_function

    @target_function.setter
    def target_function(self, value: Callable):
        if isinstance(value, Callable):
            self._target_function = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def population_initialization(self):
        return self._population_initialization

    @population_initialization.setter
    def population_initialization(self, value: Callable):
        if isinstance(value, Callable):
            self._population_initialization = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def mutation(self):
        return self._mutation

    @mutation.setter
    def mutation(self, value: Callable):
        if isinstance(value, Callable):
            self._mutation = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

    @property
    def replacement(self):
        return self._replacement

    @replacement.setter
    def replacement(self, value: Callable):
        if isinstance(value, Callable):
            self._replacement = value
        else:
            raise TypeError('Аргумент должен быть функцией.')

# строитель через наследование
class CGASettingsBuilder:
    """
    Родительский класс строителя
    """
    def __init__(self):
        self.settings = CGASettings()

    def build(self):
        return self.settings

class CGASettingsParentSelectionBuilder(CGASettingsBuilder):
    """
    Выбор родителей
    """
    def parent_selection(self, selection):
        if selection == 'СТАНДАРНЫЙ':
            self.settings.parent_selection = Selection.standart_selection
        elif selection == 'СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА':
            self.settings.parent_selection = Selection.stochastic_universal_sampling
        else:
            self.settings.parent_selection = None
        return self

class CGASettingsStopsBuilder(CGASettingsParentSelectionBuilder):
    """
    Условия останова
    """
    def stops(self, stops):
        if stops == 'КОЛИЧЕСТВО ЭПОХ':
            self.settings.stops = Stops.stopping_by_the_number_of_eras
        elif stops == 'НЕИЗМЕНЯЕМОСТЬ':
            self.settings.stops = Stops.stopping_for_the_best
        else:
            self.settings.stops = None
        return self

class CGASettingsPurposeBuilder(CGASettingsStopsBuilder):
    """
    Направление оптимизации
    """
    def purpose(self, purpose):
        if purpose == 'МИНИМУМ':
            self.settings.purpose = Purpose.sort_by_more
        elif purpose == 'МАКСИМУМ':
            self.settings.purpose = Purpose.sort_by_less
        else:
            self.settings.purpose = None
        return self

class CGASettingsRecombinationBuilder(CGASettingsPurposeBuilder):
    """
    Вид рекомбинации параметров особи
    """
    def recombination(self, recombination):
        if recombination == 'ТОЧЕЧНАЯ':
            self.settings.recombination = Recombination.point_crossing
        elif recombination == 'СЕГМЕНТИРОВАННАЯ':
            self.settings.recombination = Recombination.segmental_crossing
        elif recombination == 'РАВНОМЕРНАЯ':
            self.settings.recombination = Recombination.even_crossing
        else:
            self.settings.recombination = None
        return self

class CGASettingsPopulationInitializationBuilder(CGASettingsRecombinationBuilder):
    """
    Инициализация начальной популяции
    """
    def population_initialization(self, initialization):
        if initialization == 'СЛУЧАЙНАЯ ГЕНЕРАЦИЯ':
            self.settings.population_initialization = Population.get_new_random_population
        else:
            self.settings.population_initialization = None
        return self

class CGASettingsReplacementBuilder(CGASettingsPopulationInitializationBuilder):
    """
    Тип отбора лучших особей
    """
    def replacement(self, replacement):
        if replacement == 'ЭЛИТА':
            self.settings.replacement = Replacement.elite
        elif replacement == 'ПРОСТОЙ СРЕЗ':
            self.settings.replacement = Replacement.simple_cut
        else:
            self.settings.replacement = None
        return self