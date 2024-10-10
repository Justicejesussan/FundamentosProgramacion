"""
Ejercicio 1
    escribir un programa que pregunte al usuario su nombre
    e imprima un saludo
Entradas:
    nombre:string
salidas:
    saludo:string
"""
nombre = input( "Escribe tu nombre: " )
edad = input( "escribe edad: " )
saludo = "Holaa " + nombre + "!" + " de " + edad + " años "
print(saludo)