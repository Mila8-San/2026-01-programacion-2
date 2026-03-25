from datetime import datetime

COSTO_DE_LOS_SERVICIOS = {
    "Particular": {
        "valor_cita": 80000,
        "Limpieza": 60000, "Calzas": 80000, "Extracción": 100000, "Diagnóstico": 50000
    },
    "EPS": {
        "valor_cita": 5000,
        "Limpieza": 0, "Calzas": 40000, "Extracción": 40000, "Diagnóstico": 0
    },
    "Prepagada": {
        "valor_cita": 30000,
        "Limpieza": 0, "Calzas": 10000, "Extracción": 10000, "Diagnóstico": 0
    }
}

pacientes = []

while True:
    print("\n--- Registro Pacientes ---")
    cedula = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ")
    
    while True:
        fecha_str = input("Fecha de la cita (DD/MM/AAAA): ")
        try:
            fecha_cita = datetime.strptime(fecha_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Use DD/MM/AAAA (Ej: 25/03/2026)")

    tipos = ["Particular", "EPS", "Prepagada"]
    print("Tipo de Cliente: 1. Particular, 2. EPS, 3. Prepagada")
    idx_c = int(input("Seleccione (1-3): ")) - 1
    t_cliente = tipos[idx_c]

    atenciones = ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]
    print("Tipo de atención: 1. Limpieza, 2. Calzas, 3. Extracción, 4. Diagnóstico")
    idx_a = int(input("Seleccione (1-4): ")) - 1
    t_atencion = atenciones[idx_a]


    if t_atencion in ["Limpieza", "Diagnóstico"]:
        cantidad = 1
    else:
        while True:
            cantidad = int(input(f"Cantidad de {t_atencion}: "))
            if cantidad > 0: break
            print("La cantidad debe ser mayor a cero para este procedimiento.")

    prioridad = input("Prioridad (Normal/Urgente): ").capitalize()

    # 2. Lógica de Cálculo
    v_cita = COSTO_DE_LOS_SERVICIOS[t_cliente]["valor_cita"]
    v_atencion = COSTO_DE_LOS_SERVICIOS[t_cliente][t_atencion]
    total_pago = v_cita + (v_atencion * cantidad)

    # 3. Almacenamiento en el arreglo (Lista de diccionarios)
    pacientes.append({
        "cedula": cedula,
        "nombre": nombre,
        "fecha": fecha_str,
        "t_atencion": t_atencion,
        "total": total_pago
    })

    if input("\n¿Registrar otro paciente? (s/n): ").lower() != 's': break



pacientes.sort(key=lambda x: x['total'], reverse=True)

print("\n" + "="*50)
print(f"{'LISTA DEL CONSULTORIO':^50}")
print("="*50)
print(f"Total de Clientes atendidos: {len(pacientes)}")
print(f"Ingresos Totales: ${sum(p['total'] for p in pacientes):,}")
print(f"Pacientes para Extracción: {sum(1 for p in pacientes if p['t_atencion'] == 'Extracción')}")

print("\nLISTADO ORDENADO (POR VALOR):")
for p in pacientes:
    print(f"Fecha: {p['fecha']} | CC: {p['cedula']} | Paciente: {p['nombre']} | Total: ${p['total']:,}")

# Búsqueda final
print("\n--- Búsqueda de Paciente ---")
busqueda = input("Ingrese la cédula para consultar: ")
resultado = next((p for p in pacientes if p['cedula'] == busqueda), None)

if resultado:
    print(f"DATOS PACIENTE:\nNombre: {resultado['nombre']}\nFecha Cita: {resultado['fecha']}\nTipo de atencion: {resultado['t_atencion']}\nTotal a Pagar: ${resultado['total']:,}")
else:
    print("Paciente no encontrado en la base de datos.")