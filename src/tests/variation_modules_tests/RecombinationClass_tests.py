import unittest
import src.utils.GlobalVariables as GV
from src.utils.FileManagerClass import FileManager as fm
import random
from src.variation_modules.SelectionClass import Selection
from src.variation_modules.RecombinationClass import Recombination

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class RecombinationClassTests(unittest.TestCase):

    def test_point_crossing(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fm.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fm.get_parameters(filepath)
        random.seed(0, version=2)

        population = GV.GENETIC_ALGORITHM.population_initialization()
        population = GV.GENETIC_ALGORITHM.target_function(population)
        parents = Selection.standart_selection(population)

        '''
        Код: 110001011. Значение ЦФ: 22.0. Генотип: ['4', '6.0', '12']
        Код: 001000110. Значение ЦФ: 20.0. Генотип: ['1', '5.0', '14']
        '''

        childrens = Recombination.point_crossing(parents) # точка деления на последнем символе

        result = [childrens[0], childrens[1]]

        self.assertEqual(result, ['110001010', '001000111'])

    def test_segmental_crossing(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fm.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fm.get_parameters(filepath)
        random.seed(1, version=2)

        population = GV.GENETIC_ALGORITHM.population_initialization()
        population = GV.GENETIC_ALGORITHM.target_function(population)
        parents = Selection.standart_selection(population)

        '''
        Код: 000010001. Значение ЦФ: 19.0. Генотип: ['0', '8.0', '11']
        Код: 011001110. Значение ЦФ: 22.0. Генотип: ['2', '6.0', '14']
        '''

        childrens = Recombination.segmental_crossing(parents) # точка деления после второго символа,

        result = [childrens[0], childrens[1]]

        self.assertEqual(result, ['000010001', '011001110'])

    def test_even_crossing(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fm.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fm.get_parameters(filepath)
        random.seed(1, version=2)

        population = GV.GENETIC_ALGORITHM.population_initialization()
        population = GV.GENETIC_ALGORITHM.target_function(population)
        parents = Selection.standart_selection(population)

        '''
        Код: 000010001. Значение ЦФ: 19.0. Генотип: ['0', '8.0', '11']
        Код: 011001110. Значение ЦФ: 22.0. Генотип: ['2', '6.0', '14']
        '''

        childrens = Recombination.segmental_crossing(parents) # точка деления после второго символа,

        result = [childrens[0], childrens[1]]

        self.assertEqual(result, ['000010001', '011001110'])


if __name__ == '__main__':
    pass