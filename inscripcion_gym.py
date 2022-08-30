'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 2 : Estructuras De Control De Selección
Ejercicio 2:Calcule el monto del pago de una persona al inscribirse al gimnasio, dependiendo de si es alumno de
            la Universidad o no. Si es alumno se le hará un 50% de descuento tanto en la inscripción como en la
            mensualidad. Las cuotas sin descuento son: inscripción: 100, mensualidad: 150.
Fecha: 1 De Septiembre De 2022
'''

estudiante_activo=str(input("Eres Estudiante Universitario? (S/N) "))
estudiante_activo=estudiante_activo.upper()
inscripcion=100
mensualidad=150

while(estudiante_activo!='S' and estudiante_activo!='N'):
    print("Captura Una Opción Valida")
    estudiante_activo=str(input("Eres Estudiante Universitario? (S/N)"))

if estudiante_activo=='S':
    print("Precio de Inscripción a Pagar Es ", inscripcion*0.5)
    print("Precio Mensualidad A Pagar",mensualidad*0.5)
else:
    print("Precio de Inscripción a Pagar Es ", inscripcion)
    print("Precio Mensualidad A Pagar",mensualidad)