import random
 
def cargar():
    return int(input("Ingrese un valor entero: "))
 
def aleatorio():
    return random.randint(1,100)
 
 
def adivina():
    num = aleatorio()
    imprimir("Bienvenido al juego de adivina el numerito")
    imprimir("A ver si eres capaz de adivinarlo")
    correcto=False
    while correcto == False:
        n = cargar()
        if num==n:
            imprimir("Has ganado")
            correcto=True
        elif num<n:
            imprimir("El valor introducido es menor")
        else:
            imprimir("El valor introducido es mayor")
 
 
# función para imprimir mensajes
def imprimir(texto):
    print(texto)


    