from SOFKA_CHALLENGE.Modelo.Modelo import Juego, Usuario, Pregunta, Respuesta
from SOFKA_CHALLENGE.Usecase.constants import Constantes

def configurar_juego_default():
    user = Usuario(ident="Andres",puntaje=0)
    lista_preguntas = []
    for i in range(25):
        respuesta1 = Respuesta(texto=str(i),es_valido=True)
        respuesta2 = Respuesta(texto=str(i),es_valido=False)
        respuesta3 = Respuesta(texto=str(i),es_valido=False)
        respuesta4 = Respuesta(texto=str(i),es_valido=False)
        respuestas = [respuesta1,respuesta2,respuesta3,respuesta4]
        pregunta = Pregunta(enunciado=str(i),categoria=str(i%5),respuestas=respuestas)
        lista_preguntas.append(pregunta)
    juego = Juego(usuario=user,rondas=5,premio=0,preguntas=lista_preguntas)
    Constantes.JUEGO = juego

def configurar_juego():
    user = Usuario(ident="Andres", puntaje=0)
    lista_preguntas = []
    for i in range(25):
        respuesta1 = Respuesta(texto=str(i), es_valido=True)
        respuesta2 = Respuesta(texto=str(i), es_valido=False)
        respuesta3 = Respuesta(texto=str(i), es_valido=False)
        respuesta4 = Respuesta(texto=str(i), es_valido=False)
        respuestas = [respuesta1, respuesta2, respuesta3, respuesta4]
        pregunta = Pregunta(enunciado=str(i), categoria=str(i % 5), respuestas=respuestas)
        lista_preguntas.append(pregunta)
    juego = Juego(usuario=user, rondas=5, premio=0, preguntas=lista_preguntas)
    Constantes.JUEGO = juego