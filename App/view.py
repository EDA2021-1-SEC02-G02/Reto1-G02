﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys
 


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido. ")
    print("1- Cargar información en el catálogo. ")
    print("2- Req_1. Videos con mas vistas, tendencia en un pais con determinada categoria. ")
    print("3- Req_2. Video que mas dia ha sido trending en un pais. ")
    print("4- Req_3. Video que mas dia ha sido trending segun la categoria. ")
    print("5- Req_4. Videos con mas likes en un pais con un tag especifico. ")
    print("0- Salir. ")


def initCatalogARRAY():
    return controller.initCatalogARRAY()


def loadData(catalog):
    controller.loadData(catalog)

catalog = None


def printResults(ord_books, sample=10):
    size = lt.size(ord_books)
    if size > sample:
        print("Los primeros ", sample, " libros ordenados son:")
        i=0
        while i <= sample:
            book = lt.getElement(ord_books,i)
            print('Titulo: ' + book['title'] + ' ISBN: ' +
                book['isbn'] + ' Rating: ' + book[''])
            i+=1

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalogARRAY()
        loadData(catalog)

        print('\nLibros cargados: ' + str(lt.size(catalog['videos'])))
        print('\nvideos cargados por categorias: ' + str(lt.size(catalog['categorias'])))
        print('\nvideos cargados por paises: ' + str(lt.size(catalog['paises'])))
        firstvideo = lt.firstElement(catalog['videos'])
        print('Informacion del primer video cargado: ',
              firstvideo['title'],",",firstvideo['channel_title'],",",firstvideo['trending_date'],
              ",",firstvideo['country'],",",firstvideo['views'],",",firstvideo['likes'],",",firstvideo['dislikes'],".")

    # requerimiento 1
    
    elif int(inputs[0]) == 2:
        pais = input("buscando en el pais: ")
        categoria =input( "buscando en la categoria: ")
        cantidad= input("cantidad de videos: ")
        print(controller.requerimiento1 (catalog, pais, categoria, cantidad))

    #requerimiento 2
    
    elif int(inputs[0]) == 3:
        pais= input("buscando en el pais: ")
        print(controller.requerimiento2(catalog, pais))
    
    # requerimiento 3.
   
    elif int(inputs[0]) == 4:
        pass
   
    # requerimiento 4.
    
    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
