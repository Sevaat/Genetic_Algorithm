from src.utils.file_manager import FileManager
from src.GeneticAlgorithm import genetic_algorithm
import src.utils.GlobalVariables as GV
from src.utils.InspectionClass import Inspection


def main_ga(user_function=None):
    FileManager.open_file()
    GV.GENETIC_ALGORITHM.user_function_reference = user_function
    Inspection.inspection()
    result = genetic_algorithm()
    FileManager.save_file(result)