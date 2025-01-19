import unittest
import src.utils.GlobalVariables as GV
from src.utils.FileManagerClass import FileManager
from src.model.IndividualClass import Individual
from src.variation_modules.SelectionClass import Selection

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class SelectionClassTests(unittest.TestCase):
    def test_get_weights_1(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = FileManager.get_parameters(filepath)

        population = []
        for i in range(10):
            ind = Individual()
            ind.rank = i
            population.append(ind)

        result = Selection.get_weights(population)

        s = sum([ind.rank for ind in population])
        expected_result = [p.rank / s for p in population]

        self.assertEqual(result, expected_result)

    def test_get_weights_2(self):
        filepath = filepath_2
        GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = FileManager.get_parameters(filepath)

        population = []
        for i in range(10):
            ind = Individual()
            ind.rank = i
            population.append(ind)

        result = Selection.get_weights(population)

        s = sum([ind.rank for ind in population])
        expected_result = [(s - p.rank) / s for p in population]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
