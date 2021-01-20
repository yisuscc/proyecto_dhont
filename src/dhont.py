'''
Created on 19 ene. 2021

@author: jesus
'''
from collections import namedtuple



Votos = namedtuple('Votos', 'provincia,partido,votos')

def lee_escrutinio (ruta_votos,ruta_escaños):
    pass

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
