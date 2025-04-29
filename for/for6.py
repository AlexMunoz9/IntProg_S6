#Contar números pares hasta un límite
#Tipo de bucle: mientras
#Enunciado: Solicita un número positivo y muestra todos los números pares desde 0 hasta ese
#número.

def contar_pares(limite=0):
    for i in range(0, limite + 1, 2):
        print(i, end=" ")
def main(): 
    limite = int(input("Ingrese un numero positivo: "))
    contar_pares(limite)
    
main()
    