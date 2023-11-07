from os import system

from modulo.seno import seno
from modulo.cosseno import cosseno as cos

def tangente(angulo):
    return seno(angulo) / cos(angulo)
