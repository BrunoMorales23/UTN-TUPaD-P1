#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
num = list(range(4, 101, 4))
print(num)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!
col = ["ajedrez","series","ejercicio","anime","dormir"]
print(col[-2]) 

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []

empty_col = []
empty_col.append("ajedrez")
empty_col.append("ejercicio")
empty_col.append("anime")
print(empty_col)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

col = ["perro", "gato", "conejo", "pez"]
col[1] = "loro"
col[-1] = "oso"
print(col)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#Paso a paso, lo que hace el código visto en la imagen:
#1- Crea una lista de números, siendo estos: 8, 15, 3, 22 y 7
#2- Utiliza 'max' para identificar cuál de todos estos números es el más grande, para entonces, eliminarlo
#3- Por último, se imprime en pantalla el resultado final, que constaría de la lista, sin el valor "22"
#([8, 15, 3, 7])

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

col = list(range(10, 31, 5))
print(col[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

col = ["sedan", "polo", "suran", "gol"]
col[1] = "camioneta"
col[2] = "coupe"
print(col)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

col = []
col.append(5 * 2)
col.append(10 * 2)
col.append(15 * 2)
print(col)


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

col = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
col[2].append("jugo")
col[1][1] = "tallarines"
col[0].remove("pan")
print(col)


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla

col = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(col)