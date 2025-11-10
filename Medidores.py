class Medidor:
    def __init__(self, nombre, consumo):
        self.nombre = nombre
        self.consumo = consumo
        self.tarifa_dignidad = 110
        self.costo_normal = 0.04
        self.costo_exceso = 0.15

    def calcular_valor(self):
        if self.consumo <= self.tarifa_dignidad:
            return self.consumo * self.costo_normal
        else:
            exceso = self.consumo - self.tarifa_dignidad
            return (self.tarifa_dignidad * self.costo_normal) + (exceso * self.costo_exceso)

    def excedente(self):
        return self.consumo - self.tarifa_dignidad

    def recomendacion(self):
        if self.consumo > self.tarifa_dignidad:
            return "Cuidado su consumo excede la tarifa de la dignidad."
        else:
            return "¡Felicitaciones! Usted ha ahorrado."

    def mostrar_info(self):
        valor = self.calcular_valor()
        excedente = self.excedente()
        print(f"\nMedidor: {self.nombre}")
        print(f"Consumo: {self.consumo} kWh")
        print(f"Valor a cancelar: ${valor:.2f}")
        print(f"Excedente kWh TD: {excedente}")
        print(f"Recomendación: {self.recomendacion()}")

def menu():
    medidores = []
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar medidor")
        print("2. Mostrar consumos ordenados")
        print("3. Mostrar medidor con mayor y menor consumo")
        print("4. Mostrar tabla consolidada")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del medidor: ")
            consumo = float(input("Ingrese consumo en kWh: "))
            medidores.append(Medidor(nombre, consumo))
            print("Medidor agregado correctamente.")

        elif opcion == "2":
            if not medidores:
                print("No hay medidores registrados.")
            else:
                ordenados = sorted(medidores, key=lambda m: m.consumo)
                for m in ordenados:
                    m.mostrar_info()

        elif opcion == "3":
            if not medidores:
                print("No hay medidores registrados.")
            else:
                mayor = max(medidores, key=lambda m: m.consumo)
                menor = min(medidores, key=lambda m: m.consumo)
                print("\n--- Medidor con mayor consumo ---")
                mayor.mostrar_info()
                print("\n--- Medidor con menor consumo ---")
                menor.mostrar_info()

        elif opcion == "4":
            if not medidores:
                print("No hay medidores registrados.")
            else:
                print("\n--- Tabla Consolidada ---")
                print(f"{'Medidor':15} {'Consumo':10} {'Valor $':10} {'Excedente':12} {'Recomendación'}")
                for m in medidores:
                    print(f"{m.nombre:15} {m.consumo:<10} {m.calcular_valor():<10.2f} {m.excedente():<12} {m.recomendacion()}")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


menu()