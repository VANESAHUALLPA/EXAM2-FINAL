# POKEAPI - TRABAJO GRUPAL

#La tarea gira en torno a la PokeAPI: https://pokeapi.co/docs/v2 utilizar la API v2 y el paquete requests de Python

#Escribir un programa que tenga las siguientes opciones:

#Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.
#Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.
#Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
#Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
#Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.
#Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen


# "***********************************************************************************************"

import requests 
import json

link_pokeapi = "https://pokeapi.co/docs/v2"
pokemones = ["clefairy","bulbasaur","wormadam","charmander"]

def lista_pokemon(pokemones):
    resp = requests.get(link_pokeapi + pokemones)
    data = resp.json()
    print("****************************************")
    print("dato")

    #print = dato["weight"]




