'''
Created on 19 ene. 2021

@author: jesus
'''
from collections import namedtuple
import csv


Votos = namedtuple('Votos', 'provincia,partido,votos')

def lee_escrutinio (ruta_votos,ruta_escanos):
    dicc_escanos = dict()
    with open(ruta_votos, encoding='utf-8') as rv:
        lector = csv.reader(rv)
        next(lector)
        lista_votos = [Votos(provincia,partido,int(votos)) for provincia, partido, votos in lector]
    with open(ruta_escanos, encoding='utf-8') as re:
        lector = csv.reader(re)
        next(lector)
        for provincia, escano in lector:
            dicc_escanos[provincia] = escano
    return lista_votos, dicc_escanos
        

def calcula_provincias(lista_votos):
    pass

def calcula_partidos(lista_votos):
    pass

def calcula_provincia(lista_votos,provincia):
    pass

def calcula_diccionario_provincias(lista_votos):
    pass

def totales_por_partido(lista_votos):
    pass

def genera_diagrama_tarta(dicc, limite):
    pass

def genera_mapa_calor(dicc_2d, limite_columnas):
    pass

def calcula_tabla_porcentajes(dicc_2d):
    pass

def calcula_escaños_provincia(dicc, total_escaños, exclusion):
    pass

def calcula_tabla_escaños(dicc_2d):
    pass
