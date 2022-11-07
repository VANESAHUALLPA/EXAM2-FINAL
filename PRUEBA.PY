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
import os
# link_pokiapi = requests.get("https://pokeapi.co/api/v2/pokemon/")
# print(link_pokiapi)
# print(type(link_pokiapi.status_code))
# if(link_pokiapi.status_code==200):
#     print("PAGINA OK")
#     dato =link_pokiapi.json()
os.system('clear')

link_pokiapi = 'https://pokeapi.co/api/v2/pokemon/'
# pokemones = ['clefairy','bulbasaur','wormadam','charmander']
pokemones = ['bulbasaur','squirtle','charmander','abra']
def lista_pokemon(pokemones):
    resp = requests.get(link_pokiapi + pokemones)

    data = resp.json()

    # print(f"Nombre: {data,['name']}")
    # print(f"peso: {data['weight']}")

    lista_habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]
    print(f"Habilidades: {lista_habilidades} ")

    dicc_estadistica = {stat['stat']['name']:stat['base_stat'] for stat in data['stats']}
    print(f"Estadisticas: {dicc_estadistica} ")

    print("***************************" * 2)

for pokemon in pokemones:
    lista_pokemon(pokemon)




