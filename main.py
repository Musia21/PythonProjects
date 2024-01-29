import requests


#response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
#        headers={'Content-Type' : 'application/json','trainer_token':'a189f5d298d53f247e6e6c11f937c5ee'},
#        json={"name": "Бульбазавр", "photo": "https://dolnikov.ru/pokemons/albums/001.png"})
#
#print(f'pokemon_id: {response.text}')

#response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
#        headers={'Content-Type' : 'application/json','trainer_token':'a189f5d298d53f247e6e6c11f937c5ee'},
#        json={"pokemon_id": '28939',
#                "name": "Pika",
#                "photo": "https://dolnikov.ru/pokemons/albums/008.png"})
#print(response);

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
        headers={'Content-Type' : 'application/json','trainer_token':'a189f5d298d53f247e6e6c11f937c5ee'},
        json={"pokemon_id": '28939'})

print(f'pokeball: {response.text}')