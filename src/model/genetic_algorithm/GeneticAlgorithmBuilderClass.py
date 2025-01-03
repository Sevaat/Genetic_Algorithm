from .GeneticAlgorithmClass import GeneticAlgorithm
from src.variation_modules.PopulationClass import Population
from src.variation_modules.TargetFunctionClass import TargetFunction
from src.variation_modules.SelectionClass import Selection
from src.variation_modules.RecombinationClass import Recombination
from src.variation_modules.PurposeClass import Purpose
from src.variation_modules.ReplacementClass import Replacement
from src.variation_modules.StopsClass import Stops


class GeneticAlgorithmBuilder:
    def __init__(self, genetic_algorithm = GeneticAlgorithm()):
        self.genetic_algorithm = genetic_algorithm

    @property
    def parent_selection(self):
        return GeneticAlgorithmParentSelectionBuilder(self.genetic_algorithm)

    @property
    def stops(self):
        return GeneticAlgorithmStopsBuilder(self.genetic_algorithm)

    @property
    def purpose(self):
        return GeneticAlgorithmPurposeBuilder(self.genetic_algorithm)

    @property
    def recombination(self):
        return GeneticAlgorithmRecombinationBuilder(self.genetic_algorithm)

    @property
    def target_function(self):
        return GeneticAlgorithmTargetFunctionBuilder(self.genetic_algorithm)

    @property
    def population_initialization(self):
        return GeneticAlgorithmPopulationInitializationBuilder(self.genetic_algorithm)

    @property
    def replacement(self):
        return GeneticAlgorithmReplacementBuilder(self.genetic_algorithm)

    def build(self):
        return self.genetic_algorithm

class GeneticAlgorithmParentSelectionBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_selection(self, selection):
        if selection == 'СТАНДАРНЫЙ':
            self.genetic_algorithm.parent_selection = Selection.standart_selection
        elif selection == 'СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА':
            self.genetic_algorithm.parent_selection = Selection.stochastic_universal_sampling
        else:
            self.genetic_algorithm.parent_selection = None
        return self

class GeneticAlgorithmStopsBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_stops(self, stops):
        if stops == 'КОЛИЧЕСТВО ЭПОХ':
            self.genetic_algorithm.stops = Stops.stopping_by_the_number_of_eras
        elif stops == 'НЕИЗМЕНЯЕМОСТЬ':
            self.genetic_algorithm.stops = Stops.stopping_for_the_best
        else:
            self.genetic_algorithm.stops = None
        return self

class GeneticAlgorithmPurposeBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_purpose(self, purpose):
        if purpose == 'МИНИМУМ':
            self.genetic_algorithm.purpose = Purpose.sort_by_more
        elif purpose == 'МАКСИМУМ':
            self.genetic_algorithm.purpose = Purpose.sort_by_less
        else:
            self.genetic_algorithm.purpose = None
        return self

class GeneticAlgorithmRecombinationBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_recombination(self, recombination):
        if recombination == 'ТОЧЕЧНАЯ':
            self.genetic_algorithm.recombination = Recombination.point_crossing
        else:
            self.genetic_algorithm.recombination = None
        return self

class GeneticAlgorithmTargetFunctionBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_target_function(self, function):
        if function == 'ТЕСТОВАЯ ФУНКЦИЯ':
            self.genetic_algorithm.target_function = TargetFunction.get_result_test_function
        elif function == 'ПОЛЬЗОВАТЕЛЬСКАЯ ФУНКЦИЯ':
            self.genetic_algorithm.target_function = TargetFunction.get_result_user_defined_function
        else:
            self.genetic_algorithm.target_function = None
        return self

class GeneticAlgorithmPopulationInitializationBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_population_initialization(self, initialization):
        if initialization == 'СЛУЧАЙНАЯ ГЕНЕРАЦИЯ':
            self.genetic_algorithm.population_initialization = Population.get_new_random_population
        else:
            self.genetic_algorithm.population_initialization = None
        return self

class GeneticAlgorithmReplacementBuilder(GeneticAlgorithmBuilder):

    def __init__(self, genetic_algorithm):
        super().__init__(genetic_algorithm)

    def set_replacement(self, replacement):
        if replacement == 'ЭЛИТА':
            self.genetic_algorithm.replacement = Replacement.elite
        elif replacement == 'ПРОСТОЙ СРЕЗ':
            self.genetic_algorithm.replacement = Replacement.simple_cut
        else:
            self.genetic_algorithm.replacement = None
        return self


if __name__ == '__main__':
    pass
