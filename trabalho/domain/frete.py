class Frete:
    def __init__(self, peso, distancia, tipo_cliente, config):
        self.peso = peso
        self.distancia = distancia
        self.tipo_cliente = tipo_cliente

        self.valor_base = config["valor_base"]
        self.valor_por_km = config["valor_por_km"]
        self.desconto_vip = config["desconto_vip"]
        self.valor_minimo = config["valor_minimo"]

        self.peso_ate_1 = config["peso_ate_1"]
        self.peso_ate_5 = config["peso_ate_5"]
        self.peso_acima_5 = config["peso_acima_5"]

    def calcular(self):
        if self.peso is None or self.peso <= 0:
            raise ValueError("Peso inválido")

        if self.distancia is None or self.distancia <= 0:
            raise ValueError("Distância inválida")

        total = self.valor_base

        # cálculo por peso
        if self.peso <= 1:
            total += self.peso_ate_1
        elif self.peso <= 5:
            total += self.peso_ate_5
        else:
            total += self.peso_acima_5

        total += self.distancia * self.valor_por_km

        if self.tipo_cliente == "VIP":
            total *= (1 - self.desconto_vip)

        if total < self.valor_minimo:
            total = self.valor_minimo

        return round(total, 2)