import unittest
import src.utils.GlobalVariables as GV
from src.utils.FileManagerClass import FileManager as fm
import random
from src.variation_modules.SelectionClass import Selection

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class SelectionClassTests(unittest.TestCase):

    def test_standart_selection(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fm.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fm.get_parameters(filepath)
        random.seed(0, version=2)

        population = GV.GENETIC_ALGORITHM.population_initialization()
        population = GV.GENETIC_ALGORITHM.target_function(population)

        # [21.0, 24.0, 23.0, 22.0, 22.0, 20.0, 25.0, 18.0, 20.0, 21.0]

        parents = Selection.standart_selection(population)

        result = []
        for p in parents:
            result.append([p[0].rank, p[1].rank])

        self.assertEqual(result, [[22.0, 20.0], [22.0, 20.0], [23.0, 18.0], [20.0, 21.0], [25.0, 22.0]])

    def test_stochastic_universal_sampling(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fm.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fm.get_parameters(filepath)
        random.seed(0, version=2)

        population = GV.GENETIC_ALGORITHM.population_initialization()
        population = GV.GENETIC_ALGORITHM.target_function(population)

        # [21.0, 24.0, 23.0, 22.0, 22.0, 20.0, 25.0, 18.0, 20.0, 21.0]

        parents = Selection.stochastic_universal_sampling(population)

        result = []
        for p in parents:
            result.append([p[0].rank, p[1].rank])

        self.assertEqual(result, [[24.0, 22.0], [24.0, 25.0], [24.0, 21.0], [22.0, 25.0], [22.0, 21.0], [25.0, 21.0]])


if __name__ == '__main__':
    unittest.main()
