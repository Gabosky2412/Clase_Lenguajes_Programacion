from Modelo import *
from Vista import * 

class Controlador:
    
    #recibe como parametro el modelo y vista que el mismo esta separando o actualizando
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def updateView(self):
        pass
    
    def updateModel(self):
        pass