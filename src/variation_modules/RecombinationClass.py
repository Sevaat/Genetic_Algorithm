from abc import ABC
import random
from src.model.IndividualClass import Individual
import src.utils.GlobalVariables as GV


class Recombination(ABC):
    @staticmethod
    def point_crossing(parents: [[Individual]]) -> [Individual]:
        """
        Точечное скрещивание (случайная точка (точки) для обмена частью генотипа особей)
        :param parents: список родителей
        :return: список детей
        """
        childrens = []
        for twos in parents:
            points = Recombination.get_points(len(twos[0].code))
            children_1 = ''
            children_2 = ''
            for i in range(len(points)-1):
                children_1 += twos[i % 2].code[points[i]:points[i + 1]]
                children_2 += twos[(i + 1) % 2].code[points[i]:points[i + 1]]
            childrens.append(children_1)
            childrens.append(children_2)
        return childrens

    @staticmethod
    def segmental_crossing(parents: [[Individual]]) -> [Individual]:
        """
        Сегментное скрещивание (случайная точка (точки) для обмена частью генотипа особей с вероятностью 20%)
        :param parents: список родителей
        :return: список детей
        """
        childrens = []
        for twos in parents:
            points = Recombination.get_points(len(twos[0].code))
            children_1 = ''
            children_2 = ''
            s = True
            for i in range(0, len(points) - 1):
                if s:
                    children_1 += twos[0].code[points[i]:points[i + 1]]
                    children_2 += twos[1].code[points[i]:points[i + 1]]
                else:
                    children_1 += twos[1].code[points[i]:points[i + 1]]
                    children_2 += twos[0].code[points[i]:points[i + 1]]
                if random.randint(0, 100) < 20:
                    s = not s
            childrens.append(children_1)
            childrens.append(children_2)
        return childrens

    @staticmethod
    def even_crossing(parents: [[Individual]]) -> [Individual]:
        """
        Равномерное скрещивание (выбор каждого детского признака от родителей с вероятностью 50%)
        :param parents: список родителей
        :return: список детей
        """
        childrens = []
        for twos in parents:
            points = Recombination.get_points(len(twos[0].code))
            children_1 = ''
            children_2 = ''
            for i in range(0, len(points) - 1):
                p = random.choices(twos, weights=[50, 50], k=1)
                children_1 += p.code[points[i]:points[i + 1]]
                p = random.choices(twos, weights=[50, 50], k=1)
                children_2 += p.code[points[i]:points[i + 1]]
            childrens.append(children_1)
            childrens.append(children_2)
        return childrens

    @staticmethod
    def single_point_crossing(parents: [[Individual]]) -> [Individual]:
        """
        Одноточечное скрещивание (случайная точка для обмена частью генотипа особей)
        :param parents: список родителей
        :return: список детей
        """
        childrens = []
        for twos in parents:
            point = random.randint(1, len(twos[0].code) - 2)
            children = Individual.new_individual_by_code(twos[0].code[0:point] + twos[1].code[point:])
            childrens.append(children)
            children = Individual.new_individual_by_code(twos[1].code[0:point] + twos[0].code[point:])
            childrens.append(children)
        return childrens

    @staticmethod
    def two_point_crossing(parents: [[Individual]]) -> [Individual]:
        """
        Двухточечное скрещивание (случайные точки (2) для обмена частью генотипа особей)
        :param parents: список родителей
        :return: список детей
        """
        childrens = []
        for fours in parents:
            point_1 = random.randint(1, len(fours[0].code) - 2)
            point_2 = random.randint(1, len(fours[0].code) - 2)
            points = sorted([point_1, point_2])
            children = []
            for i, p1 in enumerate(fours):
                for p2 in fours[i + 1:]:
                    code = p1.code[0:points[0]] + p2.code[points[0]:points[1]] + p1.code[points[1]:]
                    children = Individual.new_individual_by_code(code)
                    childrens.append(children)
                    code = p2.code[0:points[0]] + p1.code[points[0]:points[1]] + p2.code[points[1]:]
                    children = Individual.new_individual_by_code(code)
                    childrens.append(children)
        return childrens

    @staticmethod
    def get_points(length: int) -> [int]:
        """
        Получение точек для рекомбинации
        :param length: длина закодированной последовательности признаков
        :return: список точек для рекомбинации
        """
        points = [random.randint(1, length - 2) for i in range(GV.PARAMETERS.recombination_point_count)]
        points.append(0)
        points.append(length)
        points = sorted(points)
        return points


if __name__ == '__main__':
    pass
