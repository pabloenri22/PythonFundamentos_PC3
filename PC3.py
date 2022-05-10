#Problema 1
def UltimaPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad

#Problema 2
def titulo(cadena):
    nueva=""
    inicioPalabra=True              #indica el inicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter.lower()
    return nueva

#Problema 3
class Circulo:
    PI = 3.14

    def __init__(self,radio):
        self.radio = radio

    def calcular_el_area(self):
        r=int(self.radio)
        print(f'el area del circulo es: {self.PI*r ** 2}')

c1=Circulo('4')
c1.calcular_el_area()

#Problema 4
class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_el_area(self):
        l=self.largo
        a=self.ancho
        print(f'el area del rectángulo es: {l*a}')
    
r1=Rectangulo(8,4)
r1.calcular_el_area()

#Problema 5
class Alumno:
    def __init__(self,nombre,numero_de_registro):
        self.nombre = nombre
        self.numero_de_registro = numero_de_registro 

    def Display(self):
        print(f'estudiante {self.nombre} con numero de registro {self.numero_de_registro}')

    def setAge(self,edad):
        self.edad = edad
        print(f'La edad del estudiante es {self.edad}')
    def setNota(self,nota):
        self.nota = nota
        print(f'La nota del alumno es {self.nota}')

a1=Alumno('Pablo','20182584H')
a1.Display()
a1.setAge(23)
a1.setNota(20)

#Problema 6
grades = input("Por favor, introduzca sus calificaciones, separadas por comas: ").split(",")
try:
    grades = [int(grade) for grade in grades]
except ValueError:
    print("Las calificaciones introducidas no tienen un formato válido.")

#Problema 7
def pascal(n):
    fila = [1]
    y = [0]
    for x in range(n):
        print(fila)
        fila=[l+r for l,r in zip(fila+y, y+fila)]
    return n>=1    
pascal(4)