#Simulador de atención en una posta médica rural

import heapq  # Para manejo de colas de prioridad
import random  # Para asignar tiempo aleatorio según gravedad

# Clase que representa a un paciente
class Paciente:
    def __init__(self, nombre, gravedad, tiempo, llegada):
        self.nombre = nombre            # Nombre del paciente
        self.gravedad = gravedad        # Nivel de gravedad: leve, moderado, crítico
        self.tiempo = tiempo            # Tiempo estimado de atención
        self.llegada = llegada          # Orden de llegada del paciente

    # Función que convierte gravedad textual en valor numérico para prioridad
    def prioridad(self):
        if self.gravedad == 'critico':
            return 1  # Prioridad más alta
        elif self.gravedad == 'moderado':
            return 2
        else:
            return 3  # Prioridad más baja

    # Permite comparar dos pacientes al ordenar (por prioridad y llegada)
    def __lt__(self, other):
        return (self.prioridad(), self.llegada) < (other.prioridad(), other.llegada)

# Lista global donde se almacenan los pacientes ingresados
pacientes = []

# Asigna tiempo de atención según nivel de gravedad
def calcular_tiempo(gravedad):
    if gravedad == "critico":
        return random.randint(10, 15)     
    elif gravedad == "moderado":
        return random.randint(30, 40)      
    elif gravedad == "leve":
        return random.randint(60, 75)     

# Función para ingresar pacientes manualmente por teclado
def agregar_paciente():
    contador = len(pacientes)  # Se usa como orden de llegada
    while True:
        print("\n--- Agregar Paciente ---")
        nombre = input("Ingrese el nombre del paciente: ")

        # Menú para seleccionar gravedad
        print("Seleccione la gravedad:")
        print("1. Leve")
        print("2. Moderado")
        print("3. Crítico")
        print("4. Cancelar")
        opcion = input("Opción: ")

        if opcion == "4":
            break  # Cancela el ingreso

        if opcion not in ["1", "2", "3"]:
            print("Opción inválida. Intente nuevamente.")
            continue

        # Traducción numérica a texto
        gravedad = {"1": "leve", "2": "moderado", "3": "critico"}[opcion]
        tiempo = calcular_tiempo(gravedad)  # Tiempo automático según gravedad

        # Crear objeto paciente y agregarlo a la lista
        paciente = Paciente(nombre, gravedad, tiempo, contador)
        pacientes.append(paciente)
        contador += 1

        print(f"Paciente agregado correctamente con tiempo estimado: {tiempo} min.\n")
        break

# Muestra todos los pacientes ordenados por gravedad y orden de llegada
def mostrar_pacientes():
    if not pacientes:
        print("\nNo hay pacientes registrados aún.")
        return

    print("\n--- Lista de pacientes registrados ---")
    pacientes_ordenados = sorted(pacientes, key=lambda p: (p.prioridad(), p.llegada))

    for i, p in enumerate(pacientes_ordenados, 1):
        print(str(i) + ". Nombre: " + p.nombre +
              " | Gravedad: " + p.gravedad.upper() +
              " | Tiempo estimado: " + str(p.tiempo) + " min" +
              " | Orden de llegada: " + str(p.llegada+1))

# Menú principal de la aplicación
def menu():
    while True:
        print("\n===== SIMULADOR DE POSTA MÉDICA =====")
        print("1. Agregar Paciente")
        print("2. Mostrar Pacientes Ordenados por Gravedad y Llegada")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_paciente()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Inicia el programa
menu()



