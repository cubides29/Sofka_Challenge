from SOFKA_CHALLENGE.Usecase.Init_game import iniciar_juego
from SOFKA_CHALLENGE.Usecase.constants import Constantes
from SOFKA_CHALLENGE.Usecase.set_game import configurar_juego_default


def main():
    configurar_juego_default()
    iniciar_juego()
    print(Constantes.JUEGO.__dict__)

main()