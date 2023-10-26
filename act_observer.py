#clase publisher se encarga de actualizar o notificar a los subscriptores

class Publisher: #funciona con 3 metodos
    def __init__(self): #metodo de inicializaicon e inicializar lista de observadores
        self._observers = []

    def addSubscriber(self, newSubscriber): #añadir una subscripcion
        self._observers.append(newSubscriber)

    def removeSubscriber(self, subscriber): #remover una suscripcion
        self._observers.remove(subscriber)

    def notifySubscribers(self, message): #enviar el mensaje de subscripcion a todos los de la lista
        for subscriber in self._observers : 
            subscriber.Update(message)
        
class Subscriber:
    
    def Update(self, message):
        pass

class Subscriberype1(Subscriber):
    
    def Update(self, message):
        print(f"Subscriber 1 recibio mensaje {message}")

class Subscriberype2(Subscriber):
    
    def Update(self, message):
        print(f"Subscriber 2 recibio mensaje {message}")


#metodo principal
if __name__ == "__main__":
    
    #crear el publisher que notifica los usuarios
    publisher1 = Publisher()

    #crear el subscriptor u "observers"
    observer1 = Subscriberype1()
    observer2 = Subscriberype2()

    canal = int(input("desea subscribirse a algun canal?\n\n1. Musica\n2. Video\n"))

    if canal == 1:
        publisher1.addSubscriber(observer1)
        
        publisher1.notifySubscribers("Felicidades, usted se subscribio al canal de Musica")
    else:
        publisher1.addSubscriber(observer2)
        
        publisher1.notifySubscribers("Felicidades, usted se subscribio al canal de Video")
        
    #agregar los subscriptores al publisher para que sean notificados
    # publisher1.addSubscriber(observer1)
    # publisher1.addSubscriber(observer2)

    #notificando a los subscriptores
    #publisher1.notifySubscribers("checking my subscribers...")