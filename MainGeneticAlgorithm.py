from src.utils.FileManagerClass import FileManager
from src.GeneticAlgorithm import genetic_algorithm


def main_ga():
    FileManager.open_file()
    result = genetic_algorithm()
    FileManager.save_file(result)


if __name__ == '__main__':
    main_ga()
