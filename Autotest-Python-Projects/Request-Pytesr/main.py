import requests 
import json

trainer_token = '7b982eacf8db1e5bdceb3222dc0b48c3'

# Создаем тренера POST
response = requests.post('https://pokemonbattle.me:5000/trainers/reg', json= {
    "trainer_token": trainer_token,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}, headers= {"Content-Type": "application/json"})

print(response.text)

# Активируем тренера POST
response_confirm = requests.post('https://pokemonbattle.me:5000/trainers/confirm_email', json= {
    "trainer_token": trainer_token
}, headers= {"Content-Type": "application/json"})

if response_confirm.status_code == 200:
    print('ok')
else:
    print('not ok')

# Создаем покемона POST
response_pokemon = requests.post('https://pokemonbattle.me:5000/pokemons', json= {
    "name": "Злюка",
    "photo": "https://w7.pngwing.com/pngs/846/590/png-transparent-pokemon-art-pokemon-3d-cartoon-fictional-character-pokemon.png"
}, headers= {"Content-Type": "application/json", "trainer_token": trainer_token })

print(response_pokemon.text)

# Сохраняем id созданного покемона
pokemon_id = response_pokemon.json()['id']

# Изменяем покемона
response_change = requests.put('https://pokemonbattle.me:5000/pokemons', 
json= {
    "pokemon_id": pokemon_id,
    "name": "Добряш"
},
headers= {"Content-Type": "application/json", "trainer_token": trainer_token })

print(response_change.text)

# Ловим покемона
response_catch = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',
{
    "pokemon_id": pokemon_id
},
headers= {"Content-Type": "application/json", "trainer_token": trainer_token })

print(response_catch.text)