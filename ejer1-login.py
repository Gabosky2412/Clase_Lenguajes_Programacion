class ClaseSingelton:
   
    _instance = None

    @classmethod
    def createInstance(self):
        if self._instance is None:
            self._instance = self.__new__(self)
        return self._instance
    
    def __str__(self) -> str:
        return"¡Soy un Singleton!"

class Strategy:
   
    def __init__(self, correo, contraseña, token, singleton_instance):
        self.correo = correo
        self.contraseña = contraseña
        self.token = token
        self.singleton_instance = singleton_instance
       
    def execute(self):
        pass
   
    def autenticar(self, correo_input, contraseña_input):
        return "usuario" == correo_input and "contraseña" == contraseña_input

class GoogleStrategy(Strategy):
   
    def execute(self):
        print("Ejecutando estrategia con Google")
        print(self.singleton_instance)
       
class FacebookStrategy(Strategy):
   
    def execute(self):
        print("Ejecutando estrategia con Facebook")
        print(self.singleton_instance)
       
class InstagramStrategy(Strategy):
   
    def execute(self):
        print("Ejecutando estrategia con Instagram")
        print(self.singleton_instance)

class Context:
   
    def __init__(self, strategy: Strategy):
        self.strategy = strategy
       
    def execute_strategy(self):
        estrategia = input("Escriba la estrategia que desea usar: ").lower()
        singleton_instance = ClaseSingelton.createInstance()
       
        if estrategia == "facebook":
            self.strategy = FacebookStrategy("correo_fb", "contraseña_fb", "token_fb", singleton_instance)
        elif estrategia == "instagram":
            self.strategy = InstagramStrategy("correo_insta", "contraseña_insta", "token_insta", singleton_instance)
        elif estrategia == "google":
            self.strategy = GoogleStrategy("correo_google", "contraseña_google", "token_google", singleton_instance)
        else:
            print("Por favor, seleccione una plataforma correcta")

        correo_input = input("Ingrese su correo: ")
        contraseña_input = input("Ingrese su contraseña: ")

        if self.strategy.autenticar(correo_input, contraseña_input):
            self.strategy.execute()
        else:
            print("Autenticación fallida. Verifique su correo y contraseña.")

# Ejemplo de uso
if __name__ == "__main__":
    context = Context(None)
    context.execute_strategy()