from src.utils.FileManagerClass import FileManager
from src.GeneticAlgorithm import genetic_algorithm
import src.utils.GlobalVariables as GV


def main_ga(user_function=None):
    FileManager.open_file()
    GV.GENETIC_ALGORITHM.user_function_reference = user_function
    result = genetic_algorithm()
    FileManager.save_file(result)


if __name__ == '__main__':
    main_ga()
