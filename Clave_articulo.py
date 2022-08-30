'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 2 : Estructuras De Control De Selección
Ejercicio 1:Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con
            descuento. El descuento lo hace en base a la clave, Si la clave es 01 el descuento es del 10% y Si la
            clave es 02 el descuento en del 20% (solo existen dos claves).
Fecha: 1 De Septiembre De 2022
'''
articulo=str(input("Nombre Del Articulo: "))
clave=str(input("Clave Del Articulo: "))
precio_or=float(input("Precio Del Articulo: "))
while((clave!="01" and clave!="02") or precio_or<0):
    print("Captura Una Clave O Precio Valido")
    clave=input("Clave Del Articulo: ")
    precio_or=float(input("Precio Del Articulo: "))

if clave=='01':
    precio_Desc=precio_or*0.9
else:
    precio_Desc=precio_or*0.8
print()
print("El Nombre Del Articulo Es:",articulo)
print("La Clave Del Articulo Es:",clave)
print("El Precio Original Del Articulo Es:",precio_or)
print("El Precio Con Descuento Del Articulo Es:",round(precio_Desc,2))
