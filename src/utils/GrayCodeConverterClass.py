from abc import ABC
import src.utils.GlobalVariables as GV


class GrayCodeConverter(ABC):
    @staticmethod
    def __get_maximum_discharge() -> [int]:
        """
        Определение наибольших разрядов параметров особи в бинарной кодировке
        :return: список значений наибольших разрядов
        """
        maximum_discharge = []
        for gene_set in GV.PARAMETERS.gene_sets:
            value = len(gene_set) - 1
            discharge = bin(value)[2:]
            maximum_discharge.append(len(discharge))
        return maximum_discharge

    @staticmethod
    def convert_to_code(genotype: [int]) -> str:
        """
        Преобразование списка значений параметров особи в код Грея с определенной разрядностью
        :param genotype: генотип особи (через индексы)
        :return: код Грея особи
        """
        gray_code = ""
        for i, gene in enumerate(genotype):
            gray_number = gene ^ (gene >> 1)
            gray_binary = bin(gray_number)[2:]
            maximum_discharge = GrayCodeConverter.__get_maximum_discharge()
            gray_binary = gray_binary.zfill(maximum_discharge[i])
            gray_code += gray_binary
        return gray_code

    @staticmethod
    def convert_from_code(code: str) -> [int]:
        """
        Преобразование кода Грея с определенной разрядностью в список значений параметров особи
        :param code: код Грея особи
        :return: генотип особи (через индексы)
        """
        genotype = []
        j = 0
        maximum_discharge = GrayCodeConverter.__get_maximum_discharge()
        for md in maximum_discharge:
            part = code[j: j + md]
            binary = part[0]
            for i in range(1, len(part)):
                if part[i] == '1':
                    if binary[i - 1] == '0':
                        binary += '1'
                    else:
                        binary += '0'
                else:
                    binary += binary[i - 1]
            genotype.append(int(binary, 2))
            j += md
        return genotype


if __name__ == '__main__':
    pass
