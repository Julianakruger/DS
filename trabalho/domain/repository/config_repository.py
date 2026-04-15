class ConfigRepository:

    def get_config(self):
        return {
            "valor_base": 10,
            "valor_por_km": 0.5,
            "peso_ate_1": 5,
            "peso_ate_5": 10,
            "peso_acima_5": 20,
            "desconto_vip": 0.20,
            "valor_minimo": 15
        }