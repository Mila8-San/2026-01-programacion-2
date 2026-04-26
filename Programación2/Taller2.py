

from datetime import datetime, date, timedelta
import random




class Cliente:
    """Representa un paciente del consultorio odontológico."""

    TIPOS_SERVICIO = [
        "Extracción dental",
        "Limpieza dental",
        "Ortodoncia",
        "Endodoncia",
        "Blanqueamiento",
        "Revisión general",
    ]
    PRIORIDADES = ["Urgente", "Normal", "Programada"]

    def __init__(self, id_cliente, nombre, telefono, tipo_servicio,
                 prioridad, fecha_cita, pieza_dental=None):
        self.id_cliente   = id_cliente
        self.nombre       = nombre
        self.telefono     = telefono
        self.tipo_servicio = tipo_servicio
        self.prioridad    = prioridad
        self.fecha_cita   = fecha_cita          # objeto date
        self.pieza_dental = pieza_dental        # número de pieza (solo extracciones)
        self.atendido     = False

    def __str__(self):
        pieza = f" | Pieza: {self.pieza_dental}" if self.pieza_dental else ""
        return (f"[{self.id_cliente:03d}] {self.nombre:<25} | "
                f"{self.tipo_servicio:<20} | "
                f"Prioridad: {self.prioridad:<10} | "
                f"Cita: {self.fecha_cita.strftime('%d/%m/%Y')}"
                f"{pieza}")



class Pila:
    """
    Implementación de una Pila (Stack) con comportamiento LIFO.
    Usada para gestionar los clientes con extracción dental URGENTE,
    apilados de la fecha más lejana a la más cercana → al desapilar
    (pop) siempre sale el de la fecha más próxima primero.
    """

    def __init__(self, nombre="Pila"):
        self._elementos = []   # lista interna
        self.nombre = nombre

    

    def apilar(self, cliente: Cliente):
        """Agrega un cliente al tope de la pila."""
        self._elementos.append(cliente)

    def desapilar(self) -> Cliente:
        """Elimina y retorna el cliente del tope de la pila."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía — no hay clientes que desapilar.")
        return self._elementos.pop()

    def tope(self) -> Cliente:
        """Retorna el cliente del tope sin eliminarlo."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._elementos[-1]

    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0

    def tamaño(self) -> int:
        return len(self._elementos)

   

    def __iter__(self):
        """Itera desde el tope hacia la base (orden de atención)."""
        return reversed(self._elementos)

    def mostrar_informe(self):
        """Imprime el informe completo de la pila."""
        separador = "═" * 80
        print(f"\n{separador}")
        print(f"  📋  INFORME DE PILA — {self.nombre.upper()}")
        print(f"  Total de clientes en pila: {self.tamaño()}")
        print(separador)

        if self.esta_vacia():
            print("  ⚠  La pila está vacía.")
        else:
            print(f"  {'#':<4} {'CLIENTE':<25} {'SERVICIO':<20} "
                  f"{'PRIORIDAD':<12} {'FECHA CITA':<12} {'PIEZA'}")
            print("─" * 80)
            for orden, cliente in enumerate(self, start=1):
                pieza = str(cliente.pieza_dental) if cliente.pieza_dental else "—"
                print(f"  {orden:<4} {cliente.nombre:<25} "
                      f"{cliente.tipo_servicio:<20} "
                      f"{cliente.prioridad:<12} "
                      f"{cliente.fecha_cita.strftime('%d/%m/%Y'):<12} "
                      f"{pieza}")
        print(separador)
        print("  ⬆  TOPE (próximo a atender)   ⬇  BASE\n")



class Cola:
    """
    Implementación de una Cola (Queue) con comportamiento FIFO.
    Usada para gestionar la agenda diaria del consultorio.
    """

    def __init__(self, nombre="Cola"):
        self._elementos = []
        self.nombre = nombre
        self._contador_atendidos = 0

   
    def encolar(self, cliente: Cliente):
        """Agrega un cliente al final de la cola."""
        self._elementos.append(cliente)

    def desencolar(self) -> Cliente:
        """Elimina y retorna el primer cliente de la cola."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía — no hay clientes en espera.")
        cliente = self._elementos.pop(0)
        cliente.atendido = True
        self._contador_atendidos += 1
        return cliente

    def frente(self) -> Cliente:
        """Retorna el primer cliente sin eliminarlo."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía.")
        return self._elementos[0]

    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0

    def tamaño(self) -> int:
        return len(self._elementos)

    

    def __iter__(self):
        return iter(self._elementos)

    def mostrar_agenda(self):
        """Imprime la agenda/cola de atención del día."""
        separador = "═" * 80
        print(f"\n{separador}")
        print(f"  📅  AGENDA DIARIA — {self.nombre.upper()}")
        print(f"  Clientes en espera: {self.tamaño()} | "
              f"Ya atendidos hoy: {self._contador_atendidos}")
        print(separador)

        if self.esta_vacia():
            print("  ✅  No quedan clientes en la cola del día.")
        else:
            print(f"  {'TURNO':<6} {'CLIENTE':<25} {'SERVICIO':<20} "
                  f"{'PRIORIDAD':<12} {'TELÉFONO'}")
            print("─" * 80)
            for turno, cliente in enumerate(self, start=1):
                marca = " ◀ SIGUIENTE" if turno == 1 else ""
                print(f"  {turno:<6} {cliente.nombre:<25} "
                      f"{cliente.tipo_servicio:<20} "
                      f"{cliente.prioridad:<12} "
                      f"{cliente.telefono}{marca}")
        print(separador + "\n")



def generar_clientes_ejemplo() -> list[Cliente]:
    """
    Genera una lista de 15 clientes de ejemplo con distintos
    servicios, prioridades y fechas de cita.
    """
    hoy = date.today()

    datos = [
        # (id, nombre, teléfono, servicio, prioridad, días_desde_hoy, pieza)
        (1,  "Ana María Torres",    "3101234567", "Extracción dental", "Urgente",   1,  18),
        (2,  "Carlos Gómez Ruiz",   "3209876543", "Limpieza dental",   "Normal",    0,  None),
        (3,  "Luisa Fernanda Ríos", "3154567890", "Extracción dental", "Urgente",   3,  36),
        (4,  "Pedro Jiménez",       "3012345678", "Ortodoncia",        "Programada",7,  None),
        (5,  "Sofía Castillo",      "3187654321", "Extracción dental", "Normal",    2,  28),
        (6,  "Andrés Morales",      "3001122334", "Extracción dental", "Urgente",   5,  47),
        (7,  "Valentina Cruz",      "3165554433", "Endodoncia",        "Urgente",   1,  None),
        (8,  "Miguel Ángel Parra",  "3223344556", "Extracción dental", "Urgente",   2,  12),
        (9,  "Isabella Vargas",     "3118877665", "Blanqueamiento",    "Normal",    4,  None),
        (10, "Juliana Ospina",      "3044433221", "Extracción dental", "Urgente",   6,  21),
        (11, "Sebastián Díaz",      "3199988776", "Revisión general",  "Normal",    0,  None),
        (12, "Camila Herrera",      "3076655443", "Extracción dental", "Normal",    3,  33),
        (13, "Felipe Guerrero",     "3132211009", "Extracción dental", "Urgente",   4,  15),
        (14, "Laura Mendoza",       "3251100998", "Limpieza dental",   "Programada",2,  None),
        (15, "Diego Ramírez",       "3083322110", "Extracción dental", "Urgente",   7,  44),
    ]

    clientes = []
    for (id_, nombre, tel, servicio, prioridad, dias, pieza) in datos:
        fecha = hoy + timedelta(days=dias)
        clientes.append(
            Cliente(id_, nombre, tel, servicio, prioridad, fecha, pieza)
        )
    return clientes



def construir_pila_urgencias(clientes: list[Cliente]) -> Pila:
    """
    Filtra clientes con:
      - Tipo de servicio: 'Extracción dental'
      - Prioridad: 'Urgente'
    Los ordena de la fecha MÁS LEJANA a la MÁS CERCANA y los apila,
    de modo que al desapilar (pop) salga siempre el de fecha más próxima.
    """
    pila = Pila("Extracciones Urgentes")

    # Filtrar
    urgentes = [
        c for c in clientes
        if c.tipo_servicio == "Extracción dental" and c.prioridad == "Urgente"
    ]

    # Ordenar de más lejana a más cercana (la más cercana quedará al tope)
    urgentes_ordenados = sorted(urgentes, key=lambda c: c.fecha_cita, reverse=True)

    for cliente in urgentes_ordenados:
        pila.apilar(cliente)

    return pila


def construir_cola_agenda(clientes: list[Cliente], fecha_dia: date) -> Cola:
    """
    Construye la cola de atención diaria con TODOS los clientes
    que tienen cita el día indicado, en el orden en que llegaron
    al registro (por id).
    """
    cola = Cola(f"Agenda {fecha_dia.strftime('%d/%m/%Y')}")

    pacientes_del_dia = sorted(
        [c for c in clientes if c.fecha_cita == fecha_dia],
        key=lambda c: c.id_cliente
    )
    for cliente in pacientes_del_dia:
        cola.encolar(cliente)

    return cola


# ════════════════════════════════════════════════════════════════════
#  SIMULACIÓN DE ATENCIÓN
# ════════════════════════════════════════════════════════════════════

def simular_llamadas_pila(pila: Pila):
    """Simula llamar y atender a los clientes de la pila de urgencias."""
    separador = "─" * 80
    print(f"\n{'═'*80}")
    print("  📞  SIMULACIÓN — LLAMADAS DE URGENCIA (PILA)")
    print(f"{'═'*80}")

    turno = 1
    while not pila.esta_vacia():
        cliente = pila.desapilar()
        print(f"\n  Turno #{turno} — Llamando a: {cliente.nombre}")
        print(f"  {separador}")
        print(f"  Teléfono  : {cliente.telefono}")
        print(f"  Servicio  : {cliente.tipo_servicio} (pieza {cliente.pieza_dental})")
        print(f"  Fecha cita: {cliente.fecha_cita.strftime('%d/%m/%Y')}")
        print(f"  ✅ Cliente notificado y registrado para atención presencial.")
        turno += 1

    print(f"\n{'═'*80}")
    print(f"  Pila vacía. Se notificaron {turno - 1} clientes urgentes.")
    print(f"{'═'*80}\n")


def simular_atencion_cola(cola: Cola):
    """Simula la atención diaria uno por uno desde la cola."""
    separador = "─" * 80
    print(f"\n{'═'*80}")
    print(f"  🦷  SIMULACIÓN — ATENCIÓN EN CONSULTORIO (COLA)")
    print(f"{'═'*80}")

    if cola.esta_vacia():
        print("  ⚠  No hay pacientes en la agenda para este día.")
        return

    turno = 1
    while not cola.esta_vacia():
        cliente = cola.desencolar()
        print(f"\n  Turno #{turno} — Atendiendo: {cliente.nombre}")
        print(f"  {separador}")
        print(f"  Servicio  : {cliente.tipo_servicio}")
        print(f"  Prioridad : {cliente.prioridad}")
        print(f"  Restantes en cola: {cola.tamaño()}")
        print(f"  ✅ Paciente atendido correctamente.")
        turno += 1

    print(f"\n{'═'*80}")
    print(f"  Atención finalizada. Se atendieron {turno - 1} paciente(s) en el día.")
    print(f"{'═'*80}\n")


# ════════════════════════════════════════════════════════════════════
#  MENÚ INTERACTIVO
# ════════════════════════════════════════════════════════════════════

def menu_principal():
    hoy = date.today()
    clientes = generar_clientes_ejemplo()

    # Construir estructuras
    pila_urgencias = construir_pila_urgencias(clientes)
    cola_hoy       = construir_cola_agenda(clientes, hoy)

    opciones = {
        "1": ("Ver todos los clientes registrados",       mostrar_todos_clientes),
        "2": ("Ver INFORME de Pila (Urgencias)",          lambda: pila_urgencias.mostrar_informe()),
        "3": ("Simular llamadas de urgencia (Pila)",      lambda: simular_llamadas_pila(pila_urgencias)),
        "4": ("Ver AGENDA diaria (Cola)",                 lambda: cola_hoy.mostrar_agenda()),
        "5": ("Simular atención del día (Cola)",          lambda: simular_atencion_cola(cola_hoy)),
        "6": ("Ver agenda de otro día",                   lambda: menu_otro_dia(clientes)),
        "0": ("Salir",                                    None),
    }

    while True:
        print("\n" + "═" * 60)
        print("  🦷  CONSULTORIO ODONTOLÓGICO — MENÚ PRINCIPAL")
        print(f"  Fecha actual: {hoy.strftime('%d/%m/%Y')}")
        print("═" * 60)
        for clave, (descripcion, _) in opciones.items():
            print(f"  [{clave}] {descripcion}")
        print("═" * 60)

        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "0":
            print("\n  👋 ¡Hasta luego! Sistema cerrado.\n")
            break
        elif opcion in opciones:
            _, accion = opciones[opcion]
            accion()
        else:
            print("  ⚠  Opción inválida. Intente de nuevo.")


def mostrar_todos_clientes(clientes=None):
    """Muestra la lista completa de clientes registrados."""
    # Se llama sin parámetros desde el menú; necesitamos acceso global
    # En este diseño simplificado, se importa el módulo y se usa globalmente.
    pass  # Ver implementación integrada en __main__


def menu_otro_dia(clientes: list[Cliente]):
    """Permite ver la agenda de otra fecha."""
    entrada = input("  Ingrese la fecha (DD/MM/AAAA): ").strip()
    try:
        fecha = datetime.strptime(entrada, "%d/%m/%Y").date()
        cola = construir_cola_agenda(clientes, fecha)
        cola.mostrar_agenda()
    except ValueError:
        print("  ⚠  Formato de fecha incorrecto. Use DD/MM/AAAA.")


# ════════════════════════════════════════════════════════════════════
#  PUNTO DE ENTRADA
# ════════════════════════════════════════════════════════════════════

def main():
    hoy = date.today()
    clientes = generar_clientes_ejemplo()

    print("\n" + "═" * 80)
    print("  🦷  CONSULTORIO ODONTOLÓGICO — SISTEMA DE GESTIÓN DE PACIENTES")
    print("       Implementación de Pilas y Colas en Python")
    print("═" * 80)

    # ── 1. Mostrar todos los clientes ────────────────────────────────
    print("\n  📋 REGISTRO GENERAL DE PACIENTES")
    print("─" * 80)
    print(f"  {'ID':<5} {'NOMBRE':<25} {'SERVICIO':<20} "
          f"{'PRIORIDAD':<12} {'FECHA CITA':<12} {'PIEZA'}")
    print("─" * 80)
    for c in clientes:
        pieza = str(c.pieza_dental) if c.pieza_dental else "—"
        print(f"  {c.id_cliente:<5} {c.nombre:<25} {c.tipo_servicio:<20} "
              f"{c.prioridad:<12} {c.fecha_cita.strftime('%d/%m/%Y'):<12} {pieza}")

    # ── 2. Construir y mostrar la PILA de urgencias ──────────────────
    pila = construir_pila_urgencias(clientes)
    pila.mostrar_informe()

    # ── 3. Simular llamadas de la PILA ───────────────────────────────
    # Trabajamos sobre una copia para no vaciar la pila del menú
    pila_copia = construir_pila_urgencias(clientes)
    simular_llamadas_pila(pila_copia)

    # ── 4. Construir y mostrar la COLA del día ───────────────────────
    cola = construir_cola_agenda(clientes, hoy)
    cola.mostrar_agenda()

    # ── 5. Simular atención de la COLA ───────────────────────────────
    cola_copia = construir_cola_agenda(clientes, hoy)
    simular_atencion_cola(cola_copia)

    # ── 6. Menú interactivo ──────────────────────────────────────────
    print("\n  ¿Desea acceder al menú interactivo? (s/n): ", end="")
    resp = input().strip().lower()
    if resp == "s":
        # Reconstruir estructuras limpias para el menú
        menu_principal()


if __name__ == "__main__":
    main()