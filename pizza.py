# Contexto

# Pizza JAT, una empresa de pizzería a nivel mundial que desea automatizar su proceso de
# solicitud de Pizzas. Para ello, se le solicita generar un prototipo rápido que abarque
# elementos básicos para que el usuario pueda pedir su pizza.


# Requerimientos

#  Requerimientos
# Crear un programa modularizado y que respete las buenas prácticas que incluya:
# 1. Un menú interactivo que permita al usuario personalizar su Pizza. Para ello,
# considerar: 
 # Que se permita cambiar el tipo de masa entre Masa Tradicional, Masa Delgada y Masa con Bordes de Queso.
 # Que se permita cambiar el tipo de salsa entre Salsa de Tomate, Salsa Alfredo, Salsa Barbecue y Salsa Pesto.
 # Que se permita modificar ingredientes (agregar y eliminar). 
 # Actualmente, la pizzería trabaja con los siguientes ingredientes: Tomate, Champiñones,
 # Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso.
 # 2. Una estimación de tiempo que tomará en que la pizza esté lista, y ofrezca la
 # posibilidad de confirmar si es que desea ordenar. 
 # El tiempo para estar lista serán 20 minutos + 2 minutos por cada ingrediente, excluyendo masa y salsa.
 # 3. Una opción que permita mostrar los ingredientes que actualmente tiene la pizza.


#--------------------------------------------------------------------------------------------------------------------#

# Definir las opciones disponibles

MASAS = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
SALSAS = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
INGREDIENTES_DISPONIBLES = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

def mostrar_opciones(titulo, opciones):
    """ Muestra un menú de opciones y devuelve la elección del cliente. """
    print(f"\n{titulo}:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    return int(input("Selecciona una opción: "))

def elegir_masa():
    """ Permite al cliente seleccionar el tipo de masa. """
    eleccion = mostrar_opciones("Opciones de masa", MASAS)
    return MASAS[eleccion - 1]

def elegir_salsa():
    """ Permite al cliente seleccionar el tipo de salsa. """
    eleccion = mostrar_opciones("Opciones de salsa", SALSAS)
    return SALSAS[eleccion - 1]

def modificar_ingredientes(ingredientes_actuales):
    """ Permite al cliente agregar o eliminar ingredientes. """
    while True:
        print("\nIngredientes disponibles para agregar o eliminar:")
        for i, ingrediente in enumerate(INGREDIENTES_DISPONIBLES, start=1):
            print(f"{i}. {ingrediente}")
        print("0. Terminar modificación")
        eleccion = int(input("Selecciona una opción (0-9): "))
        
        if eleccion == 0:
            break
        elif 1 <= eleccion <= len(INGREDIENTES_DISPONIBLES):
            ingrediente = INGREDIENTES_DISPONIBLES[eleccion - 1]
            if ingrediente in ingredientes_actuales:
                ingredientes_actuales.remove(ingrediente)
                print(f"Ingrediente '{ingrediente}' eliminado.")
            else:
                ingredientes_actuales.append(ingrediente)
                print(f"Ingrediente '{ingrediente}' agregado.")
        else:
            print("Esta opción es inválida.")
    return ingredientes_actuales

def calcular_tiempo_estimado(ingredientes):
    """ Calcula el tiempo estimado de preparación de la pizza. """
    tiempo_base = 20
    tiempo_extra = 2 * len(ingredientes)
    return tiempo_base + tiempo_extra

def mostrar_ingredientes(ingredientes):
    """ Muestra los ingredientes que el cliente eligió para la pizza. """
    if ingredientes:
        print("\nLos ingredientes de tu pizza son:")
        for ingrediente in ingredientes:
            print(f"- {ingrediente}")
    else:
        print("Hasta ahora no has añadido ingredientes.")

def confirmar_orden(ingredientes):
    """ Confirma el pedido del cliente. """
    tiempo_estimado = calcular_tiempo_estimado(ingredientes)
    print(f"\nEl tiempo estimado de preparación es de: {tiempo_estimado} minutos")
    confirmar = input("¿Confirmar tu orden? (s/n): ").lower()
    return confirmar == 's'

def main():
    """ Función principal del programa. """
    masa = None
    salsa = None
    ingredientes = []

    while True:
        print("\n--- Bienvenido a Pizza JAT ---")
        opcion = mostrar_opciones("Menú principal", [
            "Elegir tipo de masa",
            "Elegir tipo de salsa",
            "Modificar ingredientes",
            "Estimar tiempo de preparación y confirmar orden",
            "Mostrar los ingredientes actuales",
            "Salir"
        ])
        
        if opcion == 1:
            masa = elegir_masa()
            print(f"Tipo de masa seleccionado: {masa}")
        elif opcion == 2:
            salsa = elegir_salsa()
            print(f"Tipo de salsa seleccionado: {salsa}")
        elif opcion == 3:
            ingredientes = modificar_ingredientes(ingredientes)
        elif opcion == 4:
            if confirmar_orden(ingredientes):
                print(f"\n¡Orden confirmada! Tu pizza estará lista en aproximadamente {calcular_tiempo_estimado(ingredientes)} minutos.")
                break
        elif opcion == 5:
            mostrar_ingredientes(ingredientes)
        elif opcion == 6:
            print("¡Gracias por preferir Pizza JAT!")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
