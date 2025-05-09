import random

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
num = int(input("Por favor, ingresar un número entero: "))
total = len(str(abs(num)))
print(f"Su número tiene {total} dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
num = int(input("Ingresa el primer número: "))
num_end = int(input("Ingresa el segundo número: "))

if num > num_end:
    num, num_end = num_end, num

total = 0
for i in range(num + 1, num_end):
    total += i

print(f"La suma entre {num} y {num_end} es: {total}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0

while True:
    num = int(input("Ingresa un número entero (0 para terminar): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

random_num = random.randint(0, 9)
tries = 0
end_game = False

while end_game == False:
    num = int(input("Adivina el número (entre 0 y 9): "))
    tries += 1

    if num == random_num:
        end_game = True
        print(f"Adivinaste el número después de {tries} intentos.")
    else:
        print("Ese no es el número, intenta de nuevo")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente
for i in range(10, -1, -2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario

num = int(input("Por favor, declare un número entero positivo: "))

if num < 0:
    print("Número inválido, por favor, declare un número entero positivo.")
else:
    suma = sum(range(num + 1))
    print(f"La suma de todos los números entre 0 y {num} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = impares = negativos = positivos = 0

for i in range(10):
    num = int(input(f"Porfavor, introduce un número {i + 1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Negativos: {negativos}")
print(f"Positivos: {positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
suma = 0

for i in range(10):
    num = int(input(f"Porfavor, introduce un número {i + 1}: "))
    suma += num

media = suma / 100
print(f"La media de los números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Porfavor, introduce un número: ")

inv_num = num[::-1]

print(f"El número invertido es: {inv_num}")