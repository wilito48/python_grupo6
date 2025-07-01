# Simulador de Atención en una Posta Médica Rural

Este proyecto es un **simulador de atención de pacientes en una posta médica rural** implementado en Python. Permite gestionar la llegada y atención de pacientes según la gravedad de su condición, priorizando a los más críticos.

## Características
- Ingreso manual de pacientes con nombre y nivel de gravedad (leve, moderado, crítico).
- Asignación automática de tiempo estimado de atención según gravedad.
- Ordenación de pacientes por prioridad (gravedad) y orden de llegada.
- Menú interactivo en consola para agregar y visualizar pacientes.

## ¿Cómo funciona?
1. **Agregar Paciente:**
   - El usuario ingresa el nombre del paciente y selecciona el nivel de gravedad.
   - El sistema asigna un tiempo de atención aleatorio según la gravedad:
     - Crítico: 10-15 minutos
     - Moderado: 30-40 minutos
     - Leve: 60-75 minutos
   - El paciente se agrega a la lista con su orden de llegada.
2. **Mostrar Pacientes:**
   - Muestra la lista de pacientes ordenados primero por gravedad (crítico > moderado > leve) y luego por orden de llegada.

## Ejecución

Guarda el código en un archivo, por ejemplo `simulador_posta.py`, y ejecútalo con Python 3:

```bash
python simulador_posta.py
```

## Ejemplo de uso

```
===== SIMULADOR DE POSTA MÉDICA =====
1. Agregar Paciente
2. Mostrar Pacientes Ordenados por Gravedad y Llegada
3. Salir
Seleccione una opción: 1

--- Agregar Paciente ---
Ingrese el nombre del paciente: Juan Perez
Seleccione la gravedad:
1. Leve
2. Moderado
3. Crítico
4. Cancelar
Opción: 3
Paciente agregado correctamente con tiempo estimado: 12 min.
```

## Estructura del código
- **Paciente:** Clase que representa a cada paciente y su prioridad.
- **calcular_tiempo:** Asigna tiempo de atención según gravedad.
- **agregar_paciente:** Permite ingresar pacientes por teclado.
- **mostrar_pacientes:** Muestra la lista ordenada de pacientes.
- **menu:** Menú principal de la aplicación.

## Requisitos
- Python 3.x

## Notas
- El tiempo de atención es aleatorio dentro de un rango según la gravedad.
- El sistema prioriza siempre a los pacientes más graves.

---