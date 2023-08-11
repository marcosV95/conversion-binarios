continuar=""

#Definición de función para convertir un entero sin signo a su representación binaria.
def intToBit():
    """Esta función solicita al usuario un número positivo y lo convierte a binario.
    Realiza validación para asegurarse de que se ingrese un número válido.
    Devuelve la representación binaria del número."""
    
    num=input("\nIngrese un numero para tranformarlo a binario: ")
    while num.isdigit()==False:
        num=int(input("\nIngrese un numero mayor o igual a 0 para tranformarlo a binario (Evitar las letras.): "))
    num=int(num)
    numToBin=num
    binario=""

    if numToBin==0:
        binario="0" # Manejar caso especial cuando el número original es 0
    else:
        while numToBin>0:
            resto=numToBin%2
            numToBin=numToBin//2
            binario=f"{resto}"+binario

    print(f"\nEl numero {num} transformado en binario: {binario}")

# Definición de función para convertir una representación binaria a un entero sin signo.
def bitToInt():
    """Esta función solicita al usuario una cadena de bits y la convierte a un número entero.
    Realiza validación para asegurarse de que se ingrese una cadena binaria válida.
    Devuelve el número entero correspondiente a la representación binaria."""
    binario=input("Ingrese un binario: ")
    bit_Validation=binario

    #Validacion para saber si el binario ingresado es un binario valido y no un numero decimal.
    bit_Validation=bit_Validation.replace("1","")
    bit_Validation=bit_Validation.replace("0","")
    while bit_Validation!="":
        bit_Validation=input("Ingrese un binario valido: ")
        binario=bit_Validation
        bit_Validation=bit_Validation.replace("1","")
        bit_Validation=bit_Validation.replace("0","")


    numInt=0

    n=len(binario)

    #Iniciar la conversion de bit a entero
    for i in range(1,n+1):
        numInt+=int(binario[-i])*(2**(i-1))

    print(f"El binario \"{binario}\" es el numero: {numInt}") 

# Menú principal
print("\n1. Convertir binario a entero sin signo (bit to int)")
print("2. Convertir entero sin signo a binario (int to bin)")

while continuar=="":
    option=input("\nPor favor, ingrese una opcion (1 or 2): ") 

    if option=="1":
        bitToInt()
    elif option=="2":
        intToBit()
    else:
        #En caso de que el usuario ingresa cualquier otra cosa distinta de 1 y 2, regresara al inicio del bucle 
        print("\n1. Convertir binario a entero sin signo (bit to int)")
        print("2. Convertir entero sin signo a binario (int to bin)")
        print("Por favor, ingrese solo 1 o 2 como opcion.")
        continue

    continuar=input("\npress ENTER to continue ")

