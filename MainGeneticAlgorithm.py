from src.utils.FileManagerClass import FileManager
from src.GeneticAlgorithm import genetic_algorithm
import src.utils.GlobalVariables as GV
from src.utils.InspectionClass import Inspection


def main_ga(user_function=None):
    FileManager.open_file()
    GV.GENETIC_ALGORITHM.user_function_reference = user_function
    Inspection.inspection()
    result = genetic_algorithm()
    FileManager.save_file(result)


if __name__ == '__main__':
    main_ga()
