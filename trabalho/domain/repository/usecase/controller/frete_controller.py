from usecase.calcular_frete_usecase import CalcularFreteUseCase
from repository.config_repository import ConfigRepository


class FreteController:

    def calcular_frete(self, request):
        try:
            peso = request.get("peso")
            distancia = request.get("distancia")
            tipo_cliente = request.get("tipo_cliente")

            repository = ConfigRepository()
            usecase = CalcularFreteUseCase(repository)

            valor = usecase.execute(peso, distancia, tipo_cliente)

            return {
                "peso": peso,
                "distancia": distancia,
                "tipo_cliente": tipo_cliente,
                "valor_frete": valor,
                "status_code": 200
            }

        except ValueError as e:
            return {"erro": str(e), "status_code": 400}

        except Exception as e:
            return {"erro": str(e), "status_code": 500}