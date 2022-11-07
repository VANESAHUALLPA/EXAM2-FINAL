user_input2=input("Ingrese la forma que desea : ")

link_pokiapi2='https://pokeapi.co/api/v2/pokemon-shape/'

def forma_pokemon(id2):
    resp = requests.get(link_pokiapi2+id2)

    data = resp.json()

    forma_pokemon=[nombre['name'] for nombre in data['pokemon_species']]
    print(f"Lists de pokemon por forma: {forma_pokemon}")

for id2 in user_input2:
    forma_pokemon(id2)
    