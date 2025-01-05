import unittest
import src.utils.FileManagerClass as fmc
from src.utils.GrayCodeConverterClass import GrayCodeConverter as gcc
import src.utils.GlobalVariables as GV


filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class GrayCodeConverterClassTests(unittest.TestCase):

    def test_get_maximum_discharge(self):
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        result = gcc._GrayCodeConverter__get_maximum_discharge()
        '''
        количество вариантов первого признака 5 - 111
        количество вариантов второго признака 9 - 1101
        количество вариантов третьего признака 5 - 111
        '''

        self.assertEqual(result, [3, 4, 3])

    def test_convert_to_code(self):
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        genotype = [0, 7, 3]

        result = gcc.convert_to_code(genotype)
        '''
        0 - 000
        7 - 0100
        3 - 010
        '''

        self.assertEqual(result, '0000100010')

    def test_convert_from_code(self):
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        code = '0000100010'

        result = gcc.convert_from_code(code)
        '''
        0 - 000
        7 - 0100
        3 - 010
        '''

        self.assertEqual(result, [0, 7, 3])


if __name__ == '__main__':
    unittest.main()
