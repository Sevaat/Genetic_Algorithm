def test_config_init(cga_parameters, cga_settings):
    # Тест на создание нового конфига
    from src.classical_genetic_algorithm.options_ga.cga_config import Config
    from src.classical_genetic_algorithm.options_ga.cga_settings import CGASettings
    from src.classical_genetic_algorithm.options_ga.cga_parameters import CGAParameters
    config1 = Config(cga_settings[0], cga_parameters, cga_settings[1])
    assert isinstance(config1.settings, CGASettings)
    assert isinstance(config1.parameters, CGAParameters)

    config2 = Config()
    assert config1 == config2

