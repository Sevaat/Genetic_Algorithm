class Parameters:
    def __init__(self):
        self.number_of_individuals = None  # количество особей в популяции
        self.proportion_of_elite_individuals = None  # доля элитных особей
        self.number_of_eras = None  # количество эпох
        self.gene_sets = None  # данные хромосом
        self.mutation_probability = None  # вероятность мутации
        self.change_counter = None # счётчик изменений лучшей особи
        self.number_of_results = None # количество выводимых результатов


if __name__ == '__main__':
    pass