import unittest
from src.variation_modules.PurposeClass import Purpose
from src.model.IndividualClass import Individual


class PurposeClassTests(unittest.TestCase):
    def test_sort_by_more(self):
        ind_1 = Individual()
        ind_2 = Individual()
        ind_3 = Individual()
        ind_4 = Individual()
        ind_5 = Individual()

        ind_1.rank = 1
        ind_2.rank = 2
        ind_3.rank = 3
        ind_4.rank = 4
        ind_5.rank = 5

        population = [ind_1, ind_3, ind_5, ind_2, ind_4]

        result = Purpose.sort_by_more(population)

        expected_result = [ind_1, ind_2, ind_3, ind_4, ind_5]

        self.assertEqual(result, expected_result)

    def test_sort_by_less(self):
        ind_1 = Individual()
        ind_2 = Individual()
        ind_3 = Individual()
        ind_4 = Individual()
        ind_5 = Individual()

        ind_1.rank = 1
        ind_2.rank = 2
        ind_3.rank = 3
        ind_4.rank = 4
        ind_5.rank = 5

        population = [ind_1, ind_3, ind_5, ind_2, ind_4]

        result = Purpose.sort_by_less(population)

        expected_result = [ind_5, ind_4, ind_3, ind_2, ind_1]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
