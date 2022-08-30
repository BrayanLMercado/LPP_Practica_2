'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 2 : Estructuras De Control De Selección
Ejercicio 6: Realiza un programa que te muestre el día de la semana a partir de un número del 1 al 7, es decir, que
             muestre «lunes» si el día es 1, «martes» si el día es 2, y así sucesivamente. Si el día no está entre 1 y 7
             mostraremos un mensaje de “error”.
Fecha: 1 De Septiembre De 2022
'''

num_day=int(input("Captura El Día De La Semana (1-7) "))
while(num_day<1 or num_day>7):
    print("Captura Un Número De Dia Valido")
    num_day=int(input("Captura El Día De La Semana (1-7)"))

if num_day==1:
    print("El Día",num_day,"De La Semana Es Lunes")
elif num_day==2:
    print("El Día",num_day,"De La Semana Es Martes")
elif num_day==3:
    print("El Día",num_day,"De La Semana Es Miercoles")
elif num_day==4:
    print("El Día",num_day,"De La Semana Es Jueves")
elif num_day==5:
    print("El Día",num_day,"De La Semana Es Viernes")
elif num_day==6:
    print("El Día",num_day,"De La Semana Es Sabado")
else:
    print("El Día",num_day,"De La Semana Es Domingo")