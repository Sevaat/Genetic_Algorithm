import unittest
from src.model.IndividualClass import Individual
from src.model.IndividualClass import IndividualFactory
import src.utils.FileManagerClass as fmc
import src.utils.GlobalVariables as GV
import random

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class IndividualClassTests(unittest.TestCase):

    def test_transcript_individual(self):
        individual = Individual()
        individual.code = '0000100010'
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        result = individual.transcript_individual()
        '''
        0 1 2 3 4
        5.0 5.5 6.0 6.5 7.0 7.5 8.0 8.5 9.0
        10 11 12 13 14
        '''

        self.assertEqual(result, ['0', '8.5', '13'])

    def test_overstepping_1(self):
        individual = Individual()
        individual.code = '0000100010'
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        result = individual.overstepping()

        self.assertEqual(result, True)

    def test_overstepping_2(self):
        individual = Individual()
        individual.code = '0001111010'
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        result = individual.overstepping()

        self.assertEqual(result, False)

    def test_new_individual_by_code(self):
        code = '0000100010'
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        result = str(Individual.new_individual_by_code(code))

        self.assertEqual(result, "Код: 0000100010. Значение ЦФ: None. Генотип: ['0', '8.5', '13']")

    def test_new_random_individual(self):
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)
        random.seed(0, version=2)

        result = str(IndividualFactory.new_random_individual())

        self.assertEqual(result, "Код: 0100101000. Значение ЦФ: None. Генотип: ['3', '8.0', '10']")


if __name__ == '__main__':
    unittest.main()
