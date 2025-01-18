import unittest
from src.variation_modules.PurposeClass import Purpose
from src.model.IndividualClass import Individual
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.variation_modules.ReplacementClass import Replacement


filepath_1 = "../data_test/Data_Test_1.txt"


class ReplacementClassTests(unittest.TestCase):
    def test_elite_1(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = FileManager.get_parameters(filepath)

        population_2 = []
        for i in range(10):
            ind = Individual()
            ind.rank = i
            population_2.append(ind)

        population_1 = []
        for i in range(10, 20):
            ind = Individual()
            ind.rank = i
            population_1.append(ind)

        population_1 = Purpose.sort_by_less(population_1)
        population_2 = Purpose.sort_by_less(population_2)

        result = Replacement.elite(population_1, population_2)

        expected_result = [
            population_1[0],
            population_1[1],
            population_2[0],
            population_2[1],
            population_2[2],
            population_2[3],
            population_2[4],
            population_2[5],
            population_2[6],
            population_2[7]
        ]

        self.assertEqual(result, expected_result)

    def test_elite_2(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = FileManager.get_parameters(filepath)

        population_2 = []
        for i in range(4):
            ind = Individual()
            ind.rank = i
            population_2.append(ind)

        population_1 = []
        for i in range(10, 20):
            ind = Individual()
            ind.rank = i
            population_1.append(ind)

        population_1 = Purpose.sort_by_less(population_1)
        population_2 = Purpose.sort_by_less(population_2)

        result = Replacement.elite(population_1, population_2)

        expected_result = [
            population_1[0],
            population_1[1],
            population_1[2],
            population_1[3],
            population_1[4],
            population_1[5],
            population_1[6],
            population_1[7],
            population_2[0],
            population_2[1]
        ]

        self.assertEqual(result, expected_result)

    def test_simple_cut(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = FileManager.get_parameters(filepath)

        population_2 = []
        for i in range(10):
            ind = Individual()
            ind.rank = i
            population_2.append(ind)

        population_1 = []
        for i in range(10, 20):
            ind = Individual()
            ind.rank = i
            population_1.append(ind)

        population_1 = Purpose.sort_by_less(population_1)
        population_2 = Purpose.sort_by_less(population_2)

        result = Replacement.simple_cut(population_1, population_2)

        self.assertEqual(result, population_1)


if __name__ == '__main__':
    unittest.main()
