#Programa que pide al usuario ingresar una letra y una funcion que  imprima la letra siguiente en el alfabeto 
#y y la letra anterior a la ingresada
def imprimir_sig(letra):
    pos = letras [letra + 1]
    print(f'Letra siguiente: {pos}')
def imprimir_ant(letra):
    pos = letras [letra - 1]
    print(f'Letra anterior: {pos}') 

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    
    letra_ingresada = input('Ingrese una letra: ')
    if letra_ingresada in letras:
        imprimir_sig(letras.index(letra_ingresada))
        imprimir_ant(letras.index(letra_ingresada))
        salir = input('¿Desea continuar en el programa? Precione enter para'
                       'continuar, de lo contrario precione 0 + enter para salir. ')
        
        if salir == '0' :
            print('Fin del programa hasta luego.')
            break
        
    