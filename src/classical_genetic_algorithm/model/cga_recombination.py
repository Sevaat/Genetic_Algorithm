from abc import ABC
import random
from src.classical_genetic_algorithm.model.cga_individual import Individual
from src.classical_genetic_algorithm.utils.cga_duplicate_check import DuplicateCheck


class Recombination(ABC):
    @staticmethod
    def point_crossing(population: list[Individual], parents: list[tuple[Individual, Individual]]) -> list[Individual]:
        """
        Точечное скрещивание (случайная точка (точки) для обмена частью генотипа особей)
        :param population: список особей популяции
        :param parents: список родителей
        :return: список детей
        """
        children = []
        for par_par in parents:
            points = Recombination.get_points(len(par_par[0].code))
            children_1 = ''
            children_2 = ''
            for i in range(len(points)-1):
                children_1 += par_par[i % 2].code[points[i]:points[i + 1]]
                children_2 += par_par[(i + 1) % 2].code[points[i]:points[i + 1]]
            children += Recombination.child_addition(population + children, children_1, children_2)
        return children

    @staticmethod
    def segmental_crossing(population: list[Individual], parents: list[tuple[Individual, Individual]]) -> list[Individual]:
        """
        Сегментное скрещивание (случайная точка (точки) для обмена частью генотипа особей с вероятностью 20%)
        :param population: список особей популяции
        :param parents: список родителей
        :return: список детей
        """
        children = []
        for par_par in parents:
            points = Recombination.get_points(len(par_par[0].code))
            children_1 = ''
            children_2 = ''
            s = True
            for i in range(0, len(points) - 1):
                if s:
                    children_1 += par_par[0].code[points[i]:points[i + 1]]
                    children_2 += par_par[1].code[points[i]:points[i + 1]]
                else:
                    children_1 += par_par[1].code[points[i]:points[i + 1]]
                    children_2 += par_par[0].code[points[i]:points[i + 1]]
                if random.randint(0, 100) < 20:
                    s = not s
            children += Recombination.child_addition(population + children, children_1, children_2)
        return children

    @staticmethod
    def even_crossing(population: list[Individual], parents: list[tuple[Individual, Individual]]) -> list[Individual]:
        """
        Равномерное скрещивание (выбор каждого детского признака от родителей с вероятностью 50%)
        :param population: список особей популяции
        :param parents: список родителей
        :return: список детей
        """
        children = []
        for par_par in parents:
            points = Recombination.get_points(len(par_par[0].code))
            children_1 = ''
            children_2 = ''
            for i in range(0, len(points) - 1):
                p = random.choices(list(par_par), weights=[50, 50], k=1)
                children_1 += p[0].code[points[i]:points[i + 1]]
                p = random.choices(list(par_par), weights=[50, 50], k=1)
                children_2 += p[0].code[points[i]:points[i + 1]]
            children += Recombination.child_addition(population + children, children_1, children_2)
        return children

    @staticmethod
    def get_points(length: int) -> list[int]:
        """
        Получение точек для рекомбинации
        :param length: длина закодированной последовательности признаков
        :return: список точек для рекомбинации
        """
        from src.classical_genetic_algorithm.options_ga.cga_config import Config
        config = Config()
        points = [random.randint(1, length - 2) for i in range(config.parameters.recombination_point_count)]
        points.append(0)
        points.append(length)
        points = sorted(points)
        return points

    @staticmethod
    def child_addition(population: list[Individual], children_1: str, children_2: str) -> list[Individual]:
        """
        Проверка на дубликаты и добавление новых особей в список детей
        :param population: список особей популяции
        :param children_1: ребенок 1
        :param children_2: ребенок 2
        :return: список детей с возможными добавлениями
        """
        added_children = []
        children_1 = Individual.new_individual_by_code(children_1)
        if children_1 is not None:
            if DuplicateCheck.individual_addition(population, children_1):
                added_children.append(children_1)

        children_2 = Individual.new_individual_by_code(children_2)
        if children_2 is not None:
            if DuplicateCheck.individual_addition(population, children_2):
                added_children.append(children_2)

        return added_children
