import unittest
import src.utils.FileManagerClass as fmc
import src.utils.GlobalVariables as GV
from src.model.IndividualClass import Individual
from src.calculations.MutationClass import Mutation
import random

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"
filepath_3 = "../data_test/Data_Test_3.txt"


class MutationClassTests(unittest.TestCase):

    def test_mutation(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)
        random.seed(6, version=2)

        code = '001011010' # 1+7+13=21
        individual = Individual.new_individual_by_code(code)

        result = Mutation.mutation([individual])[0].code

        self.assertEqual(result, '001001010')


if __name__ == '__main__':
    unittest.main()
