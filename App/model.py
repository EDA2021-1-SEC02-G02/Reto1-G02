"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.Algorithms.Sorting import insertionsort as insert
from DISClib.Algorithms.Sorting import selectionsort as selecc
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import mergesort as marg


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalogARRAY():
    """
    inicializa el catalogo de video y su informacion
    """
    catalog = {'videos': None,
               'categorias': None,
               'paises':None,
               'paisescat': None,
               'tag':None}
    
    catalog['videos'] = lt.newList('ARRAY_LIST', cmpfunction = funcompare) 
    catalog['categorias'] = lt.newList('ARRAY_LIST' , cmpfunction = comparecategory)
    catalog['paises'] = lt.newList('ARRAY_LIST', cmpfunction = comparecountry)
    catalog['paisescat']= lt.newList('ARRAY_LIST', cmpfunction = comparecountry1)
    catalog['tag'] =lt.newList()
    
    lt.addLast(catalog['paisescat'], {})

    return catalog
"-------------------------------------------------------------------------------------------------------"
# Funciones para agregar informacion al catalogo

def addvideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    categorias = video['category_id'] 
    categorias =str(categorias)
    paises = video['country']
    newcountry(catalog, paises.strip(), video)
    newcategory(catalog, categorias.strip(), video)
    newpaiscat(catalog, paises.strip(), categorias.strip(), video)


def newcategory(catalog, categorynumber, video):
    categorias= catalog['categorias']
    poscategoria = lt.isPresent(categorias, categorynumber)
    if poscategoria >0:
        category = lt.getElement(categorias, poscategoria)
    else:
        category = addnewcategory(categorynumber)
        lt.addLast(categorias, category)
    lt.addLast(category['videos'], video)
    
    
def newcountry(catalog, countryname, video):
    paises = catalog['paises']
    pospaises = lt.isPresent(paises, countryname)
    if pospaises > 0:
        country = lt.getElement(paises, pospaises)
    else:
        country = addnewcountry(countryname)
        lt.addLast(paises, country)
    lt.addLast(country['videos'], video)
    


def newpaiscat(catalog, pais, categoria, video):
    paiscat = catalog['paisescat']
    dic = lt.getElement(paiscat, 1)
    if pais in dic:
        categorias = dic[pais]
        if categoria in categorias:
            lt.addLast(categorias[categoria], video)
        else:
            addnewcategorycat(categorias, categoria, video)
    else:
        dic = addnewcountrycat(dic, pais) 
        categorias= dic[pais]
        addnewcategorycat(categorias, categoria, video)

       

"--------------------------------------------------------------------------------------------------------"
# Funciones para creacion de datos

def addnewcategory(categorynumber):
    category = {'number_category': "", "videos": None}
    category['number_category'] = categorynumber
    category['videos'] = lt.newList('ARRAY_LIST')
    return category

def addnewcountry(countryname):
    country = {'name_country': "", "videos": None}
    country['name_country'] = countryname
    country['videos'] = lt.newList('ARRAY_LIST')
    return country


def addnewcountrycat(dic, countryname):
    dic[countryname]= {}
    return dic

def addnewcategorycat(dic, categorynumber, video):
    
    dic[str(categorynumber)]= lt.newList('ARRAY_LIST')
    lt.addLast(dic[str(categorynumber)], video)
    return dic

"----------------------------------------------------------------------------------------------------------"
# Funciones de consulta
def requerimiento1 (catalog, pais, categoria, cantidad):
    paises= lt.getElement(catalog['paisescat'],1)
    pais= paises[pais][categoria]
    lista_ordenada= qck.sort(pais, cmpVideosByViews)
    lista_retornar= lt.newList('ARRAY_LIST')
    iterador= it.newIterator(lista_ordenada)
    i=0
    while (it.hasNext(iterador)) and i<cantidad:
        elemento= it.next(iterador)
        lt.addLast(lista_retornar, elemento)
        i+=1
    return lista_retornar
    
    

def requerimiento2(catalog, pais):
    paises= catalog['paises']
    iterador= it.newIterator(paises)
    while it.hasNext(iterador):
        elemento= it.next(iterador)
        if elemento['name_country']== str(pais):
            listavideosord= elemento['videos']
            iteradorb= it.newIterator(listavideosord)
            while it.hasNext(iteradorb):
                elemento= it.next(iteradorb)
                # añadir un dict 
                
            trendingvideo= lt.firstElement(listavideosord)
            return trendingvideo
    


"---------------------------------------------------------------------------------------------------"
# Funciones utilizadas para comparar elementos dentro de una lista

def comparecategory(categorynumber1, category):
    if (categorynumber1.lower() == category['number_category'].lower()):
        return 0
    return -1


def comparecountry(countryname1, country):
    if (countryname1.lower() == country['name_country'].lower()):
        return 0
    return -1

def comparecountry1(countryname1, country):
    if (countryname1.lower() == country['pais'].lower()):
        return 0
    return -1


def comparetrending(video1, video2):
    if video1['trending_date'] < video2['trending_date']:
        return True
    else:
        return False
    

def cmpVideosByViews(video1, video2):
    if video1['views'] > video2['views']:
        return True
    else:
        return False
    
def funcompare(video1,video2):
    if video1['video_id'] > video2['video_id']:
        return 1
    if video1['video_id'] < video2['video_id']:
        return -1
    else:
        return 0

"----------------------------------------------------------------------------------------------"
# Funciones de ordenamiento

    

                
                

            

