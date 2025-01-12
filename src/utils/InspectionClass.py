from abc import ABC
import src.utils.GlobalVariables as GV
from src.variation_modules.TargetFunctionClass import TargetFunction
from src.variation_modules.StopsClass import Stops
from src.utils.GrayCodeConverterClass import GrayCodeConverter
import sys


class Inspection(ABC):
    @staticmethod
    def inspection():
        text = 'Ошибка! Проверьте данные и повторите попытку расчета. Некорректные данные:'
        Inspection.inspection_get_genetic_algorithm(text)
        Inspection.inspection_get_parameters(text)
        if text != 'Ошибка! Проверьте данные и повторите попытку расчета. Некорректные данные:':
            text[-1] = '.'
            print(text)
            sys.exit()

    @staticmethod
    def inspection_get_genetic_algorithm(text):
        if GV.GENETIC_ALGORITHM.parent_selection is None:
            text += '\nотсутствует тип выбора родителей;'
        if GV.GENETIC_ALGORITHM.stops is None:
            text += '\nотсутствуют условия останова;'
        if GV.GENETIC_ALGORITHM.purpose is None:
            text += '\nотсутствует цель оптимизации (min, max);'
        if GV.GENETIC_ALGORITHM.recombination is None:
            text += '\nотсутствует тип рекомбинации;'
        if GV.GENETIC_ALGORITHM.target_function is None:
            text += '\nотсутствует тип целевой функции;'
        if GV.GENETIC_ALGORITHM.population_initialization is None:
            text += '\nотсутствует способ инициализации новой популяции;'
        if GV.GENETIC_ALGORITHM.replacement is None:
            text += '\nотсутствует тип замены популяции;'
        if (GV.GENETIC_ALGORITHM.user_function_reference is None and
                GV.GENETIC_ALGORITHM.target_function == TargetFunction.get_result_user_defined_function):
            text += '\nвключен расчет по пользовательской функции, но функция не определена;'

    @staticmethod
    def inspection_get_parameters(text):
        flag_number_of_individuals = True
        if GV.PARAMETERS.number_of_individuals is None:
            text += '\nколичество особей в популяции не определено;'
            flag_number_of_individuals = False
        else:
            if not isinstance(GV.PARAMETERS.number_of_individuals, int):
                text += '\nколичество особей в популяции не целое число;'
                flag_number_of_individuals = False
            if GV.PARAMETERS.number_of_individuals <= 0:
                text += '\nколичество особей в популяции отрицательно;'
                flag_number_of_individuals = False

        if GV.PARAMETERS.proportion_of_elite_individuals is None:
            text += '\nдоля элитных особей не определена;'
        else:
            if not isinstance(GV.PARAMETERS.proportion_of_elite_individuals, float):
                text += '\nдоля элитных особей не вещественное число;'
            if 0 > GV.PARAMETERS.proportion_of_elite_individuals > 1:
                text += '\nдоля элитных особей отрицательно или больше 1 (единицы);'

        if GV.PARAMETERS.number_of_eras is None:
            text += '\nколичество особей в популяции не определено;'
        else:
            if not isinstance(GV.PARAMETERS.number_of_eras, int):
                text += '\nколичество эпох не целое число;'
            if GV.PARAMETERS.number_of_eras <= 0:
                text += '\nколичество эпох отрицательно;'

        flag_gene_sets = True
        if GV.PARAMETERS.gene_sets is None:
            text += '\nданные хромосом не определены;'
            flag_gene_sets = False
        else:
            if not len(GV.PARAMETERS.gene_sets):
                text += '\nотсутствуют данные хромосом;'
                flag_gene_sets = False
            if len(GV.PARAMETERS.gene_sets):
                for gs in GV.PARAMETERS.gene_sets:
                    if not len(gs):
                        text += '\nотсутствует часть данных хромосом;'
                        flag_gene_sets = False
                        break

        if GV.PARAMETERS.mutation_probability is None:
            text += '\nвероятность мутации не определена;'
        else:
            if not isinstance(GV.PARAMETERS.mutation_probability, float):
                text += '\nвероятность мутации не вещественное число;'
            if 0 > GV.PARAMETERS.mutation_probability > 1:
                text += '\nвероятность мутации отрицательна или больше 1 (единицы);'

        if GV.GENETIC_ALGORITHM.stops == Stops.stopping_for_the_best:
            if GV.PARAMETERS.change_counter is None:
                text += '\nсчётчик изменений лучшей особи не определен;'
            else:
                if not isinstance(GV.PARAMETERS.change_counter, int):
                    text += '\nсчётчик изменений лучшей особи не целое число;'
                if GV.PARAMETERS.change_counter <= 0:
                    text += '\nсчётчик изменений лучшей особи отрицательный;'

        if GV.PARAMETERS.number_of_results is None:
            text += '\nколичество выводимых результатов не определено;'
        else:
            if not isinstance(GV.PARAMETERS.number_of_results, int):
                text += '\nколичество выводимых результатов не целое число;'
            if GV.PARAMETERS.number_of_results <= 0:
                text += '\nколичество выводимых результатов отрицательно;'

        flag_recombination_point_count = True
        if GV.PARAMETERS.recombination_point_count is None:
            text += '\nколичество точек рекомбинации не определено;'
            flag_recombination_point_count = False
        else:
            if not isinstance(GV.PARAMETERS.recombination_point_count, int):
                text += '\nколичество точек рекомбинации не целое число;'
                flag_recombination_point_count = False
            if GV.PARAMETERS.recombination_point_count < 0:
                text += '\nколичество точек рекомбинации отрицательно;'
                flag_recombination_point_count = False
            if GV.PARAMETERS.recombination_point_count == 0:
                text += '\nколичество точек рекомбинации равно нулю;'
                flag_recombination_point_count = False

        if flag_gene_sets and flag_recombination_point_count:
            n = sum(GrayCodeConverter._GrayCodeConverter__get_maximum_discharge())
            if GV.PARAMETERS.recombination_point_count > n - 1:
                text += f'\nколичество точек рекомбинации больше или равно длине генотипа {n};'

        if GV.PARAMETERS.number_of_recurring_individuals is not None:
            if not isinstance(GV.PARAMETERS.number_of_recurring_individuals, int):
                text += '\nколичество повторяющихся особей не целое число;'
            if GV.PARAMETERS.number_of_recurring_individuals <= 0:
                text += '\nколичество повторяющихся особей отрицательно;'

        if flag_gene_sets:
            n = 1
            for gs in GV.PARAMETERS.gene_sets:
                n *= len(gs)
            if flag_number_of_individuals and GV.PARAMETERS.number_of_individuals > n / 2:
                text += f'\nпревышено количество особей в популяции (менее {n / 2});'
