def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
    return a / b
    else:
    return "error: division por 0"

print("Ingrese el primer número:")
num1 = float(input())

print("Ingrese el segundo número:")
num2 = float(input())

print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. multiplicar")
print("4. dividir")
print("5. salir")

while true:
    try:
option = input("\nseleccione una opcion (1-5): ")
if option == '5':
   print("hasta luego")
    break
opcion = int(input())

if opcion == 1:
    resultado = suma(num1, num2)
    print("La suma es:", resultado)
elif opcion == 2:
    resultado = resta(num1, num2)
    print("La resta es:", resultado)
elif option == 3:
    resultado = multiplicar(num1, num2)
    print(f"resultado: {num1} * {num2} = {resultado}")
elif option == 4:
    resultado = dividir(num1, num2)
    print(f"resultado:{num1} / {num2} {resultado}")

else:
    print("opcion no valida. por favor selecciona del 1 al 5,")

