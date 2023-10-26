class DataLoader:

    #atributos de la clase: son comunes a todos los objetos de la clase

    #atributos de instancia: son especificos de cada objeto

    #atributos de instancia (estaticos):
    numloads = 0

    #atributos de instancia (son inicializados cada que se instancia un nuevo metodo)
    #(en metodo de inicializacion)
    def __init__(self,filename) -> None:
        self.filename

    def LoadData(self):
        numloads = numloads+1


class Persona:

    #caracteristica general, de todas las personas
    especie = "homo sapiens"
    galaxia = "via lactea"
    vida_prom = "75"

    #caracteristica especifica, de cada persona es diferente
    #metodo de inicializacion(metodo que CREA un nuevo objeto)
    def __init__(self, pNombre, pEdad, pEstatura, pPeso, PGenero) -> None:

        #atributos de instancia, es decir se inciializan cada que se crea un nuevo objeto o persona
        self.nombre = pNombre
        self.edad = pEdad
        self.estatura = pEstatura
        self.peso = pPeso
        self.genero = PGenero

    #sobrecargamos la funcion print del objeto para que imprima los atributos
    #es decir lo que queremos que se imprima ira aqui
    def __str__(self) -> str:
        if self.genero == "H":
            return(f"{self.nombre} es un {self.especie} de {self.edad} años que vive en la {self.galaxia} y genero hombre")
        if self.genero == "M":
            return(f"{self.nombre} es un {self.especie} de {self.edad} años que vive en la {self.galaxia} y genero mujer")
       

#si tiene sus propios atribuos debe tener su propio metodo de inicializcion

#si tiene su propio metodo de inicializacion, debera tener su propio pritn o sobrecargar dicho print
#y asi imprima los datos o lo requerido y/o que queramos

class Estudiante(Persona):

    def __init__(self, pNombre, pEdad, pEstatura, pPeso, PGenero, pCarrera, pSemestre) -> None:

        #usa la inicializacion de la superclase que es la que hereda, clase persona
        super().__init__(pNombre, pEdad, pEstatura, pPeso, PGenero)
        self.carrera = pCarrera
        self.semestre = pSemestre

    def __str__(self) -> str:
        return(f"{self.nombre} es un estudiante de {self.carrera} y en su semestre numero {self.semestre}")

class Empleado(Persona):

    def __init__(self, pNombre, pEdad, pEstatura, pPeso, PGenero, pCargo, pSalario) -> None:

        super().__init__(pNombre, pEdad, pEstatura, pPeso, PGenero)
        self.cargo = pCargo
        self.salario = pSalario

    def __str__(self) -> str:
        return(f"{self.nombre} es un emplado con {self.salario} por pago y {self.edad} años y un cargo de {self.cargo}")