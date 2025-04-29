#leer numero y dar la tabla de multiplicar
def tablamultiplicar(numero=0):
    for i in range(1, 13):
        print(f"{numero} x {i} = {numero * i}")
def main():
    numero = int(input("Ingrese un numero: "))
    tablamultiplicar(numero)
    
main()