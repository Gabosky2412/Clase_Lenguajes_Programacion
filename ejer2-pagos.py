class Strategy:

    def __init__(self, n_tarjeta, ccv, fecha, pago) -> None:
        self.n_tarjeta = n_tarjeta
        self.ccv = ccv
        self.fecha = fecha
        self.pago = pago

    def execute(self):
        pass

    def autenticar(self):
        return self.n_tarjeta >= 9 and self.fecha >= 4 and self.ccv >= 3

class Pay_U(Strategy):
    def execute(self):
        print("\nEjecutando estrategia con Pay U")

        print("El pago será en pesos colombianos, total de:", self.pago)
        conversion = int(input("\nDesea pasar dicho valor a dólares?\n1. Si\n2. No: "))

        if conversion == 1:
            self.currency_converter = COLToUSDAdapter()
            converted_payment = self.currency_converter.convert(self.pago, "COL")
            print("El pago se convertirá a dólares estadounidenses, total de:", converted_payment, "USD")

            print("\n\nEl pago se realizo correctamente y se descontara de su tarjeta, gracias y vuelva pronto\n\n")
        else:
            print("El pago se mantendrá en pesos colombianos.")

            print("\n\nEl pago se realizo correctamente y se descontara de su tarjeta, gracias y vuelva pronto\n\n")

class MercadoPago(Strategy):
    def execute(self):
        print("\nEjecutando estrategia con Mercado Pago")
        
        print("El pago será en pesos colombianos, total de:", self.pago)
        conversion = int(input("\nDesea pasar dicho valor a dólares?\n1. Si\n2. No: "))

        if conversion == 1:
            self.currency_converter = COLToUSDAdapter()
            converted_payment = self.currency_converter.convert(self.pago, "COL")
            print("El pago se convertirá a dólares estadounidenses, total de:", converted_payment, "USD")

            print("\n\nEl pago se realizo correctamente y se descontara de su tarjeta, gracias y vuelva pronto\n\n")
        else:
            print("El pago se mantendrá en pesos colombianos.")

            print("\n\nEl pago se realizo correctamente y se descontara de su tarjeta, gracias y vuelva pronto\n\n")

class PayPal(Strategy):
    def execute(self):
        print("\nEjecutando estrategia con PayPal")
        
        print("El pago será en pesos colombianos, total de:", self.pago)
        conversion = int(input("\nDesea pasar dicho valor a dólares?\n1. Si\n2. No: "))

        if conversion == 1:
            self.currency_converter = COLToUSDAdapter()
            converted_payment = self.currency_converter.convert(self.pago, "COL")
            print("El pago se convertirá a dólares estadounidenses, total de:", converted_payment, "USD")

            print("\n\nEl pago se realizo correctamente y se descontara de su tarjeta, gracias y vuelva pronto\n\n")
        else:
            print("El pago se mantendrá en pesos colombianos.")

            print("\n\nEl pago se realizo correctamente y se descontara de su tarjeta, gracias y vuelva pronto\n\n")

class COLToUSDAdapter:
    def convert(self, amount, currency):
        if currency == "COL":
            return amount / 4200 
        return amount

class Context:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        print("Por favor seleccione el medio de pago:")
        print("1. Pay U\n2. Mercado Pago\n3. PayPal")
        estrategia = int(input())

        pago = float(input("\nPor favor ingrese el valor del pago: "))
        n_tarjeta = int(input("\nPor favor ingrese el numero de su tarjeta: "))
        fecha = int(input("Por favor ingrese la fecha de vencimiento de su tarjeta: "))
        ccv = int(input("Por favor ingrese el codigo de seguridad de su tarjeta: "))

        if estrategia == 1:
            self.strategy = Pay_U(n_tarjeta, ccv, fecha, pago)
        elif estrategia == 2:
            self.strategy = MercadoPago(n_tarjeta, ccv, fecha, pago)
        elif estrategia == 3:
            self.strategy = PayPal(n_tarjeta, ccv, fecha, pago)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        if self.strategy.autenticar():
            self.strategy.execute()
        else:
            print("Autenticación fallida. Verifique los datos de su tarjeta.")

# Ejemplo de uso
if __name__ == "__main__":
    context = Context(None)
    context.execute_strategy()
