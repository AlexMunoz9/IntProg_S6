#Tabla de multiplicar de un número
#Tipo de bucle: para
#nunciado: Pide al usuario un número entero positivo y muestra su tabla de multiplicar del 1 al 10.

def tablamultiplicar(numero=0):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
def main():
    numero = int(input("Ingrese un numero: "))
    tablamultiplicar(numero)
    
main()