#singelton clasico
#patron de diseño
#se usa para una cola de impresion, de seccion de un usuario, cosas dond eno se ocupe la misma accion se repita
# 1. evita el acceso concurrente a un recurso compartido
# 2. tener un punto accesible global a un recurso

# - formas de implementacion
# 1. singelton a nivel de modulo
# 2. singelton clasico

class ClaseSingelton:

    _instance_ = None
   
    def __init__(self) -> None:
        raise RuntimeError("invocar la funcion create_instance paa crear objeto")
   
    #metodos de objeto o de instancia
    def enqueueDocument(self, filename, formar):
        pass

    def despachoDocumento(self, filename):
        pass

    def eliminarDocumento(self,filename):
        pass

    #classmethod es un metodo estatico global
    #un metodo estatico no necesita ser instanciado para que el singelton salga correctamente
    #crea la instancia peros olo una instancia del objeto, solo un objeto
    @classmethod
    def createInstance(self):
        if self._instance_ is None:
            #solo hace una instancia una sola vez cuando no se a instanciado ningun otro objeto
            self._instance_ = self.__new__(self)
        #__new__ lo usa internamente _init_ para crear una nueva instacia de la clase

        return self._instance_
   
#------------- fin implementacion de singelton ------------------------#

# printerPool1 = ClaseSingelton()
# printerPool2 = ClaseSingelton()

printerPool1 = ClaseSingelton.createInstance() #se llama como un metodo estatico, no metodo de objeto
printerPool2 = ClaseSingelton.createInstance()

print(printerPool1)
print(printerPool2)
print(printerPool1 == printerPool2)

#----------------------------------------------------------------------------------------------------------------------------------#

#adapter
#patron estructural
#adapta una peticion de un cliente al formato requerido por y para el mismo que pueda ser utilizado
class Adaptee:
    
    def __init__(self):
        pass

    def request_trans(self):
        return "peticion adaptada al requerimeinto del cliente"
    
class Cliente:
    
    def __init__(self):
        pass
    
    def request(self):
        return "peticion del cliente no compatible con la clase adaptada"
    
class Adapter:
    
    def __init__(self,adaptee:Adaptee):
        self.adaptee = adaptee
        
    def request(self):
        return self.adaptee.request_trans()
    
#ejemplo implementacion adapter
pdf_reader = Cliente()
word_reader = Adaptee()

print(Adapter(word_reader).request)

#----------------------------------------------------------------------------------------------------------------------------------#

#strategy
#comportamiento
#ejemplo la geolocalizacion, calcular el descuento de una matricula para la universidad USC

#clase que define una estrategia en general 
class Strategy:
    
    def execute():
        pass
    
class ConcreteStrategyA(Strategy):
    
    def execute(self):
        print ("ejecutando estrategia contreta A")
        
class ConcreteStrategyB(Strategy):
    
    def execute(self):
        print ("ejecutando estrategia contreta B")

#la clase context es la que permite al cliente ejecutar la estrategia correspondiente:
class Context:
    
    def __init__(self,strategy:Strategy):
        self.strategy = strategy
        
    def execute_strategy(self):
        self.strategy.execute()
        
#ejemplo de uso del patron strategy:

#usando estrategia A
strategyA = ConcreteStrategyA()
#le pasamos el contexto y por mas metodos deberia de elegir cual estrategia usar, en este caso se la asignamos
contexto_str1 = Context(strategyA)
result_str1 = contexto_str1.execute_strategy()

#usando estrategia B
strategyB = ConcreteStrategyB()
contexto_str2 = Context(strategyB)
result_str2 = contexto_str2.execute_strategy()