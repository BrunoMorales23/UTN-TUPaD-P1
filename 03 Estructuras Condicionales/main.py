import getpass
from statistics import mode, median, mean
import random

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
try:
    num = input("Por favor, deposite su edad...")

    if int(num) >= 18:
        print(f"Es mayor de edad.")
    else:
        print(f"Es menor de edad.")
except ValueError:
    print(f"El valor depositado no corresponde a un número")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”
try:
    num = input("Por favor, deposite su nota...")

    if int(num) >= 6:
        print(f"Aprobado!")
    else:
        print(f"Desaprobado...")
except ValueError:
    print(f"El valor depositado no corresponde a un número")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par".
try:
    num = input("Por favor, deposite un número...")

    if (int(num) % 2 == 0):
        print(f"Ha ingresado un número par...")
    else:
        print(f"Por favor, ingrese un número par...")

except ValueError:
    print(f"El valor depositado no corresponde a un número")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
try:
    num = input("Por favor, deposite su edad...")

    if int(num) < 12:
        print(f"Usted es un Niño/a")
    elif int(num) >= 12 | int(num) < 18:
        print(f"Usted es un Adolescente")
    elif int(num) >= 18 | int(num) < 30:
        print(f"Usted es un Adulto/a joven")
    else:
        print(f"Usted es un Adulto/a mayor")
except ValueError:
    print(f"El valor depositado no corresponde a un número")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
password = getpass.getpass("Por favor, deposite su contraseña...")

if len(password) >= 8 and len(password) <= 14:
    print(f"Ha ingresado una contraseña correcta...")
else:
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres...")

#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
num = [random.randint(-100, 100) for i in range(50)]
#Se modifica la formula propuesta, a fin de que exista la chance de sesgo negativo

if mean(num) > median(num) > mode(num):
    print(f"Determinamos, sesgo positivo.")
elif mean(num) < median(num) < mode(num):
    print(f"Determinamos, sesgo negativo.")
elif mean(num) == median(num) == mode(num):
    print(f"Determinamos, sin sesgo.")
else:
    print(f"Sesgo indeterminado.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
texto = input("Por favor, ingrese un texto aleatorio, lo que más te guste!  ")

if texto.lower()[len(texto)-1] in "aeiou":
    print(texto + "!")
else:
    print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. 
texto = input("Por favor, ingrese su nombre...")
salida = False

while salida == False:
    print("Por favor, seleccione entre las siguientes opciones: 1 para MAYÚSCULAS. 2 para minúsculas. 3 para poner solo la primer letra en Mayúsculas. 0 para salir.")
    try:
        num = input("¿Qué desea hacer?  ")

        if int(num) == 1:
            print(texto.upper())
            salida = True
        elif int(num) == 2:
            print(texto.lower())
            salida = True
        elif int(num) == 3:
            print(texto.title())
            salida = True
        elif int(num) == 0:
            salida = True
        else:
            print("Opción no válida")
    except ValueError:
        print(f"El valor depositado no corresponde a un número")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
num = input("Por favor, asigne un valor en escala de Richter para el terremoto sucedido o a suceder   ")
try:
    if int(num) < 3:
        print("Muy leve (Imperciptible)")
    elif int(num) >= 3 and int(num) < 4:
        print("Leve (ligeramente perceptible)")
    elif int(num) >= 4 and int(num) < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif int(num) >= 5 and int(num) < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif int(num) >= 6 and int(num) < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    elif int(num) >= 7:
        print("Extremo (puede causar graves daños a gran escala)")
except ValueError:
        print(f"El valor depositado no corresponde a un número")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
salida = False

while salida == False:
    texto = input("¿En qué emisferio te encuentras? (N/S)   ")
    if texto.upper() == "N" or texto.upper() == "S":
        salida = True
    else:
        print("Por favor, selecciona un hemisferio válido...")

salida = False
while salida == False:
    try:
        mes = input("¿Qué mes del año es? (Por favor, deposite el número correspondiente del mes. Ej: 'Marzo = 3')   ")
        dia = input("¿Qué día del año es?   ")

        if int(dia) > 31 or int(mes) > 12:
            print(f"Valor para día/mes inválido.")
        else:
                if texto.upper() == "S":
                    if int(mes) == 12 and int(dia) >= 21 and int(dia) <= 31:
                        print(f"Su temporada es Verano")
                    elif int(mes) == 1 or int(mes) == 2:
                        print(f"Su temporada es Verano")
                    elif int(mes) == 3 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Verano")
                    elif int(mes) == 3 and int(dia) >= 21 and int(dia) <= 31:
                        print(f"Su temporada es Otoño")
                    elif int(mes) == 4 or int(mes) == 5:
                        print(f"Su temporada es Otoño")
                    elif int(mes) == 6 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Otoño")
                    elif int(mes) == 6 and int(dia) >= 21 and int(dia) <= 30:
                        print(f"Su temporada es Invierno")
                    elif int(mes) == 7 or int(mes) == 8:
                        print(f"Su temporada es Invierno")
                    elif int(mes) == 9 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Invierno")
                    elif int(mes) == 9 and int(dia) >= 21 and int(dia) <= 30:
                        print(f"Su temporada es Primavera")
                    elif int(mes) == 10 or int(mes) == 11:
                        print(f"Su temporada es Primavera")
                    elif int(mes) == 12 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Primavera")
                elif texto.upper() == "N":
                    if int(mes) == 12 and int(dia) >= 21 and int(dia) <= 31:
                        print(f"Su temporada es Invierno")
                    elif int(mes) == 1 or int(mes) == 2:
                        print(f"Su temporada es Invierno")
                    elif int(mes) == 3 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Invierno")
                    elif int(mes) == 3 and int(dia) >= 21 and int(dia) <= 31:
                        print(f"Su temporada es Primavera")
                    elif int(mes) == 4 or int(mes) == 5:
                        print(f"Su temporada es Primavera")
                    elif int(mes) == 6 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Primavera")
                    elif int(mes) == 6 and int(dia) >= 21 and int(dia) <= 30:
                        print(f"Su temporada es Verano")
                    elif int(mes) == 7 or int(mes) == 8:
                        print(f"Su temporada es Verano")
                    elif int(mes) == 9 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Verano")
                    elif int(mes) == 9 and int(dia) >= 21 and int(dia) <= 30:
                        print(f"Su temporada es Otoño")
                    elif int(mes) == 10 or int(mes) == 11:
                        print(f"Su temporada es Otoño")
                    elif int(mes) == 12 and int(dia) >= 1 and int(dia) <= 20:
                        print(f"Su temporada es Otoño")
                salida = True
    except ValueError:
        print(f"El valor depositado no corresponde a un número")
