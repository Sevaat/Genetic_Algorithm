import unittest
import src.utils.FileManagerClass as fmc
from src.variation_modules.SelectionClass import Selection
from src.variation_modules.PurposeClass import Purpose
from src.variation_modules.RecombinationClass import Recombination
from src.variation_modules.TargetFunctionClass import TargetFunction
from src.variation_modules.PopulationClass import Population
from src.variation_modules.ReplacementClass import Replacement


filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class FileManagerClassTests(unittest.TestCase):

    def  test_get_genetic_algorithm_1(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = str(type(ga))

        self.assertEqual(result, "<class 'src.model.genetic_algorithm.GeneticAlgorithmClass.GeneticAlgorithm'>")

    def  test_get_genetic_algorithm_2(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.parent_selection

        self.assertEqual(result, Selection.standart_selection)

    def  test_get_genetic_algorithm_3(self):
        filepath = filepath_2
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.parent_selection

        self.assertEqual(result, Selection.stochastic_universal_sampling)

    def  test_get_genetic_algorithm_4(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.purpose

        self.assertEqual(result, Purpose.sort_by_less)

    def  test_get_genetic_algorithm_5(self):
        filepath = filepath_2
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.purpose

        self.assertEqual(result, Purpose.sort_by_more)

    def  test_get_genetic_algorithm_6(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.recombination

        self.assertEqual(result, Recombination.point_crossing)

    def  test_get_genetic_algorithm_7(self):
        filepath = filepath_2
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.recombination

        self.assertEqual(result, Recombination.segmental_crossing)

    def  test_get_genetic_algorithm_8(self):
        filepath = filepath_3
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.recombination

        self.assertEqual(result, Recombination.even_crossing)

    def  test_get_genetic_algorithm_9(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.target_function

        self.assertEqual(result, TargetFunction.get_result_test_function)

    def  test_get_genetic_algorithm_10(self):
        filepath = filepath_2
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.target_function

        self.assertEqual(result, TargetFunction.get_result_user_defined_function)

    def  test_get_genetic_algorithm_11(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.population_initialization

        self.assertEqual(result, Population.get_new_random_population)

    def  test_get_genetic_algorithm_12(self):
        filepath = filepath_1
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.replacement

        self.assertEqual(result, Replacement.elite)

    def  test_get_genetic_algorithm_13(self):
        filepath = filepath_2
        ga = fmc.FileManager.get_genetic_algorithm(filepath)

        result = ga.replacement

        self.assertEqual(result, Replacement.simple_cut)


if __name__ == '__main__':
    unittest.main()