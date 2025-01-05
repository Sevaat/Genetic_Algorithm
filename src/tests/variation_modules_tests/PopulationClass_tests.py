import unittest
import src.utils.FileManagerClass as fmc
from src.variation_modules.PopulationClass import Population
import src.utils.GlobalVariables as GV
import random

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class PopulationClassTests(unittest.TestCase):

    def test_get_new_random_population(self):
        filepath = filepath_3
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)
        random.seed(0, version=2)

        population = Population.get_new_random_population()
        result = []
        for p in population:
            result.append(p.code)

        self.assertEqual(result, ['0100101000', '0111100010', '0100110010'])


if __name__ == '__main__':
    unittest.main()
