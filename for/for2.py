#leer un numero ingresado por el usuario
#mostrar la letra a por cada numero del 1 al numero
#ingresado por el usuario ejemplo, Numero: 3
#a
#aa
#aaa

def mostrar_letra(numero):
    for i in range(numero+1):
        print(f"a" *i)
    
def main():
    numero = int(input("Ingrese un numero: "))
    mostrar_letra(numero)
    
main()
