from SOFKA_CHALLENGE.Modelo.Modelo import Usuario
from SOFKA_CHALLENGE.Usecase import constants
from SOFKA_CHALLENGE.Usecase.set_game import configurar_juego_default


def iniciar_juego():
    if constants.Constantes.JUEGO == None:
        configurar_juego_default()

    while True:
        jugador = input("ingrese usuario")
        usuario = Usuario(ident=jugador,puntaje=0)
        constants.Constantes.JUEGO.usuario = usuario

        if jugador in constants.Constantes.LISTA_JUGADORES:
            print("el nombre ya existe, intente nuevamente")

        else:
            jugar(jugador)
            break


def jugar(jugador:str):

    print("========== Bienvenido ========")
    print(jugador)
    juego = constants.Constantes.JUEGO
    ronda = 0
    while ronda<5:
        preguntas = [prf for prf in juego.preguntas
                     if prf.categoria == str(ronda)]
        print(preguntas[0].enunciado)
        print("las opciones son:")
        respuestas = preguntas[0].respuestas
        for respuesta in respuestas:
            print(respuesta.texto)

        seleccion = int(input("seleccione la respuesta correcta"))
        while seleccion not in [0,1,2,3]:
            print("ingrese una opcion valida")
            seleccion = int(input("seleccione la respuesta correcta"))
        if respuestas[seleccion].es_valido:
            print("Felicitaciones, escogiste la respuesta correcta")
            juego.usuario.puntaje  +=1
            print("Felicitaciones, has ganado un punto:")
            print("Ahora tienes:")
            print(juego.usuario.puntaje)
        else:
            print("has perdido")
            break
        ronda+=1

