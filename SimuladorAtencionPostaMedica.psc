Proceso PostaMedica
    Dimension pacientes[100]
    Dimension gravedades[100]
    Dimension tiempos[100]
    Dimension llegadas[100]
	
	Definir pacientes Como Cadena
	Definir gravedades, tiempos, llegadas Como Entero
    Definir totalPacientes, i Como Entero
    Definir opcion, nombre Como Cadena
	
    totalPacientes <- 0
	
    Mientras Verdadero Hacer
        Escribir ""
        Escribir "=====> SIMULADOR DE POSTA MÉDICA <====="
        Escribir "1. Agregar Paciente"
        Escribir "2. Mostrar Pacientes"
        Escribir "3. Salir"
        Escribir "Seleccione una opción:"
        Leer opcion
		
        Si opcion = "1" Entonces
            Si totalPacientes < 100 Entonces
                totalPacientes <- totalPacientes + 1
                Escribir "Ingrese el nombre del paciente:"
                Leer nombre
                pacientes[totalPacientes] <- nombre
				
                Escribir "Seleccione la gravedad:"
                Escribir "1. Leve"
                Escribir "2. Moderado"
                Escribir "3. Crítico"
                Leer gravedades[totalPacientes]
				
                Segun gravedades[totalPacientes] Hacer
                    1:
                        tiempos[totalPacientes] <- Aleatorio(60, 75)
                    2:
                        tiempos[totalPacientes] <- Aleatorio(30, 40)
                    3:
                        tiempos[totalPacientes] <- Aleatorio(10, 15)
                    De Otro Modo:
                        tiempos[totalPacientes] <- 0
                FinSegun
				
                llegadas[totalPacientes] <- totalPacientes
                Escribir "Paciente registrado con tiempo estimado: ", tiempos[totalPacientes], " min"
            SiNo
                Escribir "Límite de pacientes alcanzado."
            FinSi
			
        SiNo
            Si opcion = "2" Entonces
                Si totalPacientes = 0 Entonces
                    Escribir "No hay pacientes registrados."
                SiNo
                    Escribir "--- Lista de pacientes ---"
                    Para i <- 1 Hasta totalPacientes Con Paso 1
                        Escribir i, ". Nombre: ", pacientes[i], " | Gravedad: ", gravedades[i], " | Tiempo estimado: ", tiempos[i], " min | Orden de llegada: ", llegadas[i]
                    FinPara
                FinSi
            SiNo
                Si opcion = "3" Entonces
                    Escribir "Saliendo del programa..."
					salir <- Verdadero
                SiNo
                    Escribir "Opción inválida. Intente nuevamente."
                FinSi
            FinSi
        FinSi
    FinMientras
FinProceso





