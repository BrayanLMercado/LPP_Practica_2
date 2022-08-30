'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 2 : Estructuras De Control De Selección
Ejercicio 4: Programa que compara si el valor de a y b es mayor a c (a, b y c son capturados por el usuario).
Fecha: 1 De Septiembre De 2022
'''

a=float(input("Captura Un Número (A): "))
b=float(input("Captura Un Número (B): "))
c=float(input("Captura Un Número (C): "))

if (a>c and b>c):
    print("A y B Son Mayores Que C")
elif(a==c and b==c):
    print("A y B Son Iguales A C")
else:
    print("A y B No Son Mayores Que C")