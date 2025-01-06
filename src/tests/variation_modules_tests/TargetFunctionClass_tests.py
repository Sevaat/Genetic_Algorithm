import unittest
import src.utils.FileManagerClass as fmc
import src.utils.GlobalVariables as GV
from src.model.IndividualClass import Individual
import random
from src.variation_modules.TargetFunctionClass import TargetFunction

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class TargetFunctionClassTests(unittest.TestCase):

    def test_get_result_test_function(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        code = '001011010' # 1+7+13=21
        individual = Individual.new_individual_by_code(code)

        result = TargetFunction.get_result_test_function([individual])[0].rank

        self.assertEqual(result, 21)


if __name__ == '__main__':
    unittest.main()
