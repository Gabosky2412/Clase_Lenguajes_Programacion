class Strategy:

    def __init__(self, distancia) -> None:
        self.distancia = distancia

    def execute(self):
        pass

class MaP(Strategy):
    def execute(self):
        print("\nEjecutando estrategia con Metro(s) a Pie(s)")

        print("La conversion sera de: ", self.distancia, "Metros")

        self.currency_converter = Distancia_MaP()
        converted_payment = self.currency_converter.convert(self.distancia, "Metros")
        print("La conversion finalizo, total de:", converted_payment, "Pies")

        print("\n\nEspero le haya sido de ayuda, vuelva pronto!\n\n")

class PaM(Strategy):
    def execute(self):
        print("\nEjecutando estrategia con Pie(s) a Metro(s)")

        print("La conversion sera de: ", self.distancia, "Pies")

        self.currency_converter = Distancia_PaM()
        converted_payment = self.currency_converter.convert(self.distancia, "Pies")
        print("La conversion finalizo, total de:", converted_payment, "Metros")

        print("\n\nEspero le haya sido de ayuda, vuelva pronto!\n\n")

class Distancia_MaP:
    def convert(self, amount, currency):
        if currency == "Metros":
            return amount / 0.3048
        return amount
    
class Distancia_PaM:
    def convert(self, amount, currency):
        if currency == "Pies":
            return amount / 3.28
        return amount

class Context:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        print("Bienvenido al conversor de unidades!")
        print("Por favor seleccione la adaptacion que desea hacer:")
        print("1. Metro(s) a Pie(s)\n2. Pie(s) a Metro(s)")
        estrategia = int(input())

        distancia = float(input("\nPor favor ingrese el valor que desea transformar:  "))

        if estrategia == 1:
            self.strategy = MaP(distancia)
        elif estrategia == 2:
            self.strategy = PaM(distancia)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        self.strategy.execute()

# Ejemplo de uso
if __name__ == "__main__":
    context = Context(None)
    context.execute_strategy()