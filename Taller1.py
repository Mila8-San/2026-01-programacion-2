
def ejecutar_programa():
    clientes = []
    

    precios = {
        "Particular": {
            "valor_cita": 80000,
            "atenciones": {"Limpieza": 60000, "Calzas": 80000, "Extracción": 100000, "Diagnóstico": 50000}
        },
        "EPS": {
            "valor_cita": 5000,
            "atenciones": {"Limpieza": 0, "Calzas": 40000, "Extracción": 40000, "Diagnóstico": 0}
        },
        "Prepagada": {
            "valor_cita": 30000,
            "atenciones": {"Limpieza": 0, "Calzas": 10000, "Extracción": 10000, "Diagnóstico": 0}
        }
    }

    continuar = "s"
    while continuar.lower() == "s":
        print("\n--- Captura de Datos del Cliente ---")
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")

        while True:
            tipo_cliente = input("Tipo de Cliente (Particular, EPS, Prepagada): ").capitalize()
            if tipo_cliente in precios: break
            print("Error: Tipo no válido.")

        while True:
            tipo_atencion = input("Tipo de Atención (Limpieza, Calzas, Extracción, Diagnóstico): ").capitalize()
            if tipo_atencion in ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]: break
            print("Error: Atención no válida.")

        while True:
            cantidad = int(input("Cantidad: "))
            if tipo_atencion in ["Limpieza", "Diagnóstico"]:
                if cantidad == 1: break
                else: print("Para Limpieza/Diagnóstico la cantidad debe ser 1.")
            else:
                if cantidad > 0: break
                else: print("La cantidad debe ser mayor a 0.")

        prioridad = input("Prioridad (Normal, Urgente): ")
        fecha = input("Fecha de la cita (DD/MM/AAAA): ")

        v_cita = precios[tipo_cliente]["valor_cita"]
        v_atencion_unitario = precios[tipo_cliente]["atenciones"][tipo_atencion]
        total_pagar = v_cita + (v_atencion_unitario * cantidad)

        cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "tipo_atencion": tipo_atencion,
            "valor_total": total_pagar
        }
        clientes.append(cliente)

        continuar = input("\n¿Desea registrar otro cliente? (s/n): ")

    total_clientes = len(clientes)
    ingresos_totales = sum(c["valor_total"] for c in clientes)
    clientes_extraccion = sum(1 for c in clientes if c["tipo_atencion"] == "Extracción")

    print("\n" + "="*30)
    print(f"Total Clientes: {total_clientes}")
    print(f"Ingresos Totales: ${ingresos_totales:,.0f}")
    print(f"Clientes para Extracción: {clientes_extraccion}")

    for i in range(len(clientes)):
        for j in range(0, len(clientes) - i - 1):
            if clientes[j]["valor_total"] < clientes[j+1]["valor_total"]:
                clientes[j], clientes[j+1] = clientes[j+1], clientes[j]

    print("\nLista de Clientes ordenada por valor (Mayor a Menor):")
    for c in clientes:
        print(f"Cédula: {c['cedula']} - Nombre: {c['nombre']} - Total: ${c['valor_total']:,.0f}")

    busqueda = input("\nIngrese cédula a buscar: ")
    encontrado = False
    for c in clientes:
        if c["cedula"] == busqueda:
            print(f"¡Encontrado! Cliente: {c['nombre']}, Valor pagado: ${c['valor_total']:,.0f}")
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

ejecutar_programa()