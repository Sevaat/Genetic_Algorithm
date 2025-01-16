import unittest
from src.model.IndividualClass import Individual
import src.utils.FileManagerClass as fmc
import src.utils.GlobalVariables as GV
from src.utils.DuplicateCheckClass import DuplicateCheck

filepath_1 = "../data_test/Data_Test_1.txt"
filepath_2 = "../data_test/Data_Test_2.txt"


class DuolicateCheckClassTests(unittest.TestCase):

    def test_individual_addition_1(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        population = [
            Individual.new_individual_by_code('1'),
            Individual.new_individual_by_code('1')
        ]
        individual = Individual.new_individual_by_code('1')

        result = DuplicateCheck.individual_addition(population, individual)

        self.assertEqual(result, False)

    def test_individual_addition_2(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        population = [
            Individual.new_individual_by_code('1'),
            Individual.new_individual_by_code('1')
        ]
        individual = Individual.new_individual_by_code('2')

        result = DuplicateCheck.individual_addition(population, individual)

        self.assertEqual(result, True)

    def test_individual_addition_3(self):
        filepath = filepath_1
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        population = [
            Individual.new_individual_by_code('1'),
            Individual.new_individual_by_code('2')
        ]
        individual = Individual.new_individual_by_code('1')

        result = DuplicateCheck.individual_addition(population, individual)

        self.assertEqual(result, True)

    def test_individual_addition_4(self):
        filepath = filepath_2
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        population = [
            Individual.new_individual_by_code('1'),
            Individual.new_individual_by_code('2')
        ]
        individual = Individual.new_individual_by_code('1')

        result = DuplicateCheck.individual_addition(population, individual)

        self.assertEqual(result, True)

    def test_individual_addition_5(self):
        filepath = filepath_2
        GV.GENETIC_ALGORITHM = fmc.FileManager.get_genetic_algorithm(filepath)
        GV.PARAMETERS = fmc.FileManager.get_parameters(filepath)

        population = [
            Individual.new_individual_by_code('1'),
            Individual.new_individual_by_code('1')
        ]
        individual = Individual.new_individual_by_code('1')

        result = DuplicateCheck.individual_addition(population, individual)

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
