'''
Created on 19 ene. 2021

@author: jesus
'''
from dhondt import *






# rutas 
ruta_votos_and_2015 = ('../data/and-2015-votos.csv')
ruta_escanos_and_2015 = ('../data/and-2015-escaдos.csv')
ruta_votos_and_2018 = ('../data/and-2018-votos.csv')
ruta_escanos_and_2018 = ('../and-2018-escaдos.csv')
ruta_escanos_cat_2017 = ('../data/cat-2017-escaдos.csv')
ruta_votos_cat_2017 = ('../data/cat-2017-votos.csv')
ruta_votos_gen_2015 = ('../data/generales-2015-votos.csv')
ruta_escanos_gen_2015= ('../data/generales-2015-escaдos.csv')
ruta_escanos_gen_2016 = ('../data/generales-2016-escaдos.csv')
ruta_votos_gen_2016 = ('../data/generales-2016-votos.csv')

#unpackings
lista_votos_and_2015, dicc_escanos_and_2015 = lee_escrutinio(ruta_votos_and_2015,ruta_escanos_and_2015)
lista_votos_and_2018, dicc_escanos_and_2018 = lee_escrutinio(ruta_votos_and_2018,ruta_escanos_and_2018)
lista_votos_cat_2017,dicc_escanos_cat_2017 =lee_escrutinio(ruta_votos_cat_2017,ruta_escanos_cat_2017)
lista_votos_gen_2015, dicc_escanos_gen_2015 = lee_escrutinio(ruta_votos_gen_2015,ruta_escanos_gen_2015 )
lista_votos_gen_2016, dicc_escanos_gen_2016 = lee_escrutinio(ruta_votos_gen_2016,ruta_escanos_gen_2016)

# tests 