import pytest

from src.utils.data_verification import DataVerification

def test_is_int():
    assert DataVerification.is_int("123") == True
    assert DataVerification.is_int("0") == True
    assert DataVerification.is_int("-42") == True
    assert DataVerification.is_int("3.14") == False
    assert DataVerification.is_int("abc") == False
    assert DataVerification.is_int("") == False
    assert DataVerification.is_int(None) == False
    assert DataVerification.is_int([]) == False

def test_is_float():
    assert DataVerification.is_float("123") == True
    assert DataVerification.is_float("0") == True
    assert DataVerification.is_float("-42") == True
    assert DataVerification.is_float("3.14") == True
    assert DataVerification.is_float("abc") == False
    assert DataVerification.is_float("") == False
    assert DataVerification.is_float(None) == False
    assert DataVerification.is_float([]) == False

def test_verification():
    # int, нестрогое неравенство
    assert DataVerification.verification("10", "int", 5, 15, False, False) == 10
    assert DataVerification.verification("5", "int", 5, 10, False, False) == 5
    assert DataVerification.verification("10", "int", 5, 10, False, False) == 10
    # int, строгое неравенство
    assert DataVerification.verification("10", "int", 5, 15, True, True) == 10
    # float, нестрогое неравенство
    assert DataVerification.verification("3.5", "float", 3.0, 4.0, False, False) == 3.5
    assert DataVerification.verification("4.0", "float", 3.5, 4.0, False, False) == 4.0
    # float, строгое неравенство
    assert DataVerification.verification("3.7", "float", 3.5, 4.0, True, True) == 3.7

    # некорректный тип
    with pytest.raises(TypeError):
        DataVerification.verification("abc", "int", 1, 10, False, False)
    with pytest.raises(TypeError):
        DataVerification.verification("abc", "float", 1.0, 10.0, False, False)
    # нарушение ограничения по нижней границе
    with pytest.raises(ValueError):
        DataVerification.verification("2", "int", 3, 10, False, False)
    with pytest.raises(ValueError):
        DataVerification.verification("3", "int", 3, 10, True, False)
    with pytest.raises(ValueError):
        DataVerification.verification("3.0", "float", 3.0, 5.0, True, False)
    # нарушение ограничения по верхней границе
    with pytest.raises(ValueError):
        DataVerification.verification("11", "int", 1, 10, False, False)
    with pytest.raises(ValueError):
        DataVerification.verification("10", "int", 1, 10, False, True)
    with pytest.raises(ValueError):
        DataVerification.verification("5.0", "float", 1.0, 5.0, False, True)