from abc import ABC
from typing import Union


class DataVerification(ABC):
    @staticmethod
    def is_int(text: str) -> bool:
        """
        Проверять является ли строка целым числом
        :param text: строка
        :return: True - является; False - не является
        """
        try:
            int(text)
            return True
        except TypeError:
            return False
        except ValueError:
            return False

    @staticmethod
    def is_float(text: str) -> bool:
        """
        Проверять является ли строка числом с плавающей точкой
        :param text: строка
        :return: True - является; False - не является
        """
        try:
            float(text)
            return True
        except TypeError:
            return False
        except ValueError:
            return False

    @staticmethod
    def verification(
        input_value: str,
        input_type: str,
        bottom: Union[float, int],
        top: Union[float, int],
        strict_bottom: bool,
        strict_top: bool,
    ) -> Union[float, int]:
        """
        Проверять вводимые данные по типу и величине из строки
        :param input_value: число в виде строки
        :param input_type: тип, по которому ведется проверка
        :param bottom: нижний предел значения числа
        :param top: верхний предел значения числа
        :param strict_bottom: строгое ли неравенство по нижней границе: False - не строгое, True - строгое
        :param strict_top: строгое ли неравенство по верхней границе: False - не строгое, True - строгое
        :return: конвертированное число из строки
        """
        value = None

        if input_type == "int":
            if DataVerification.is_int(input_value):
                value = int(input_value)
            else:
                raise TypeError
        elif input_type == "float":
            if DataVerification.is_float(input_value):
                value = float(input_value)
            else:
                raise TypeError

        if strict_bottom:
            condition_1 = bottom < value
        else:
            condition_1 = bottom <= value

        if strict_top:
            condition_2 = value < top
        else:
            condition_2 = value <= top

        if condition_1 and condition_2:
            return value
        else:
            raise ValueError
