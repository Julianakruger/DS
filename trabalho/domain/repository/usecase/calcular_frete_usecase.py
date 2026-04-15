from domain.frete import Frete


class CalcularFreteUseCase:

    def __init__(self, config_repository):
        self.config_repository = config_repository

    def execute(self, peso, distancia, tipo_cliente):
        config = self.config_repository.get_config()

        frete = Frete(peso, distancia, tipo_cliente, config)

        return frete.calcular()