'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 2 : Estructuras De Control De Selección
Ejercicio 3:Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese
            rango, muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación
            usando una tabla definida
Fecha: 1 De Septiembre De 2022
'''

calif=float(input("Calificación Del Estudiante (0.0 a 1.0) "))
while(calif<0 or calif>1):
    print("Captura Una Calificaión Dentro Del Rango")
    calif=float(input("Calificación Del Estudiante (0.0 a 1.0) "))
if calif>=0.9:
    print(calif,"Sobresaliente")
elif calif>=0.8 and calif <0.9:
    print(calif,"Notable")
elif calif>=0.7 and calif<0.8:
    print(calif,"Bien")
elif calif>=0.6 and calif<0.7:
    print(calif,"Suficiente")
else:
    print(calif,"Insuficiente")