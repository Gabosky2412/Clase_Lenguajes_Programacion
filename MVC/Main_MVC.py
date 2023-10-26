from Controlador import *
from Modelo import *
from Vista import * 

#metodo principal del modulo:

if __name__ == "__main__":
    modelo = Model1()
    vista = view_1()
    
    controlador = Controlador(modelo,vista)
    
    #logica de la aplciacion completa en la que el controlador va a poner a
    #interactuar al modelo y la vista
    #............