def test_convert_to_code(cga_config):
    # Тест на успешный перевод данных особи в код Грея
    from src.classical_genetic_algorithm.utils.cga_gray_code_converter import GrayCodeConverter
    genotype = [0, 2, 0]
    code = GrayCodeConverter.convert_to_code(genotype)
    assert code == '001100'

    genotype =[3]
    code = GrayCodeConverter.convert_to_code(genotype)
    assert code == '10'

    genotype = [5, 5]
    code = GrayCodeConverter.convert_to_code(genotype)
    assert code == '111111'

def test_convert_from_code(cga_config):
    # Тест на успешный перевод кода Грея в данные особи
    from src.classical_genetic_algorithm.utils.cga_gray_code_converter import GrayCodeConverter
    code = '001100'
    genotype = GrayCodeConverter.convert_from_code(code)
    assert genotype == [0, 2, 0]

    code = '000111'
    genotype = GrayCodeConverter.convert_from_code(code)
    assert genotype == [0, 1, 2]

    code = '010101'
    genotype = GrayCodeConverter.convert_from_code(code)
    assert genotype == [1, 1, 1]