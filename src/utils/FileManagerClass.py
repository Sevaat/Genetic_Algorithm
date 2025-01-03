from tkinter import filedialog
from src.model.ParametersClass import *
from src.model.genetic_algorithm.GeneticAlgorithmBuilderClass import GeneticAlgorithmBuilder
import src.utils.GlobalVariables as GV


class FileManager:
    @staticmethod
    def save_file(result):
        filepath = filedialog.asksaveasfilename(
            title='Сохранение файла',
            defaultextension='txt',
            initialfile='Result.txt'
        )
        if filepath != "":
            with open(filepath, "w") as file:
                for res in result:
                    file.write(f'{res}\n')

    @staticmethod
    def open_file():
        filepath = filedialog.askopenfilename(
            title='Загрузка файла',
            defaultextension='txt',
            initialfile='Data.txt'
        )
        if filepath != "":
            GV.GENETIC_ALGORITHM = FileManager.get_genetic_algorithm(filepath)
            GV.PARAMETERS = FileManager.get_parameters(filepath)

    @staticmethod
    def get_genetic_algorithm(filepath):
        ga = None
        gab = GeneticAlgorithmBuilder()
        with open(filepath, "r") as file:
            for line in file:
                data = line.strip().split(':')
                if data[0] == 'Тип выбора родителей':
                    ga = gab.parent_selection.set_selection(data[1].strip())
                elif data[0] == 'Условия останова':
                    ga = gab.stops.set_stops(data[1].strip())
                elif data[0] == 'Цель оптимизации (min, max)':
                    ga = gab.purpose.set_purpose(data[1].strip())
                elif data[0] == 'Тип рекомбинации':
                    ga = gab.recombination.set_recombination(data[1].strip())
                elif data[0] == 'Целевая функция':
                    ga = gab.target_function.set_target_function(data[1].strip())
                elif data[0] == 'Способ инициализации новой популяции':
                    ga = gab.population_initialization.set_population_initialization(data[1].strip())
                elif data[0] == 'Замена популяции':
                    ga = gab.replacement.set_replacement(data[1].strip())
                else:
                    continue
        ga = gab.build()
        return ga

    @staticmethod
    def get_parameters(filepath):
        parameters = Parameters()
        gene_sets = []
        with open(filepath, "r") as file:
            for line in file:
                data = line.strip().split(':')
                if data[0] == 'Количество особей в популяции':
                    parameters.number_of_individuals = int(data[1].strip())
                elif data[0] == 'Доля элитных особей':
                    parameters.proportion_of_elite_individuals = float(data[1].strip())
                elif data[0] == 'Количество эпох':
                    parameters.number_of_eras = int(data[1].strip())
                elif data[0] == 'Вероятность мутации':
                    parameters.mutation_probability = float(data[1].strip())
                elif data[0] == 'Cчетчик изменений лучшей особи':
                    parameters.change_counter = int(data[1].strip())
                    GV.counter = int(data[1].strip())
                elif data[0] == 'Количество выводимых результатов':
                    parameters.number_of_results = int(data[1].strip())
                elif data[0] == 'Количество точек рекомбинации':
                    parameters.recombination_point_count = int(data[1].strip())
                elif data[0] == 'Ген':
                    gene_sets.append(data[1].strip().split())
                elif data[0] == 'Ген (н, к, ш)':
                    gene_set = []
                    start, end, step = [float(i) for i in data[1].strip().split()]
                    while start <= end:
                        gene_set.append(start)
                        start += step
                    gene_sets.append(gene_set)
                else:
                    continue
        parameters.gene_sets = gene_sets
        return parameters


if __name__ == '__main__':
    pass
