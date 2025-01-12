from src.calculations.MutationClass import Mutation


class GeneticAlgorithm:
    def __init__(self):
        self.parent_selection = None # тип выбора родителей
        self.stops = None # условия останова
        self.purpose = None # цель оптимизации (min, max)
        self.recombination = None # тип рекомбинации
        self.target_function = None # целевая функция
        self.population_initialization = None # способ инициализации новой популяции
        self.mutation = Mutation.mutation
        self.replacement = None # тип замены популяции
        self.user_function_reference = None # ссылка на пользовательскую функцию


if __name__ == '__main__':
    pass
