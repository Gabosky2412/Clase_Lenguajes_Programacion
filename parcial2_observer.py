class Publisher: 
    def __init__(self): 
        self._observers = []

    def addSubscriber(self, newSubscriber):
        self._observers.append(newSubscriber)

    def removeSubscriber(self, subscriber): 
        self._observers.remove(subscriber)

    def notifySubscribers(self, message): 
        for subscriber in self._observers : 
            subscriber.Update(message)

    def notifyAlert(self, message):
        for subscriber in self._observers : 
            subscriber.Update(message)    
        
class Subscriber:
    
    def Update(self, message):
        pass

class Subscriberype1(Subscriber):
    
    def Update(self, message):
        print(f"Tiene un nuevo mensaje: {message}")

    def __str__(self) -> str:
        return "Alerta por meteoritos!!!"
    
if __name__ == "__main__":
    
    publisher1 = Publisher()

    subs = int(input("desea recibir notificacion por posibles alertas meteorologicas?\n\n1. SI\n2. NO\n"))

    if subs == 1:
        
        observer1 = Subscriberype1()
        publisher1.addSubscriber(observer1)
        
        publisher1.notifySubscribers("Felicidades, usted se ha suscrito al canal de alertas meteorologicas")

        publisher1.notifyAlert("Alerta meteorologica activa!!!")

        publisher1.notifySubscribers("La alerta funciono a la perfeccion, todo esta correcto")

        renov = int(input("Desea seguir activo en el canal de notificaciones?\n\n1. SI\n2. NO\n"))

        if renov == 1:
            publisher1.notifySubscribers("Perfecto, seguira estando suscrito")
        elif renov == 2:
            publisher1.notifySubscribers("Perfecto, sera retirado muy pronto")
            publisher1.removeSubscriber
            publisher1.notifySubscribers("listo, ya no esta en la base de datos, tenga un buen dia!")

        
    elif subs == 2:
        print("Usted ha decidido no ser notificado por alertas meteorologicas")

    else :
        print("Numero equivocado, intente de nuevo")