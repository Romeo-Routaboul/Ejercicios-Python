def eleccion_usuario():
    while True:
        eleccion = input("escoge entre piedra, papel o tijera: ").capitalize()
        if eleccion in ["Piedra", "Papel", "Tijera"]:
            return eleccion
        else:
            print("Por favor introduce una opcion valida")
