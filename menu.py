def mostrar_menu():
    print("Menu de batalla")
    print("1. Atacar")
    print("2. Defender")
    print("3. Objetos")
    print("4. Salir")




while True:
    mostrar_menu()
    opcion = input("Elige una opción (1 - 4)")

    if opcion == "1":
        print("Provocaste 20 puntos de daño")
    elif opcion == "2":
        print("Tu defensa subió 30 puntos")
    elif opcion == "3":
        print("Inventario vacío")
    elif opcion == "4":
        print("Saliste de la batalla")
        break
    else:
        print("Opción inválida. Intente de nuevo...")