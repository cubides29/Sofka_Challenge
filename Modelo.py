from dataclasses import dataclass
from typing import List


@dataclass
class Respuesta:
    texto: str
    es_valido: bool


@dataclass
class Pregunta:
    categoria: int
    respuestas: List[Respuesta]
    enunciado: str


@dataclass
class Usuario:
    ident: str
    puntaje: int


@dataclass
class Juego:
    rondas: int
    usuario: Usuario
    premio: int
    preguntas: List[Pregunta]




