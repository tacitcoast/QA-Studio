import requests
import pytest

# Проверяем, что ответ запроса get/pokemons приходит с кодом 200
def test_status_code_pokemons():
    response = requests.get('https://pokemonbattle.me:5000/pokemons')
    assert response.status_code == 200

# Проверяем, что ответ запроса get/trainers приходит с кодом 200
def test_status_code_trainers():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

#Проверяем, что в ответе приходит строчка с именем моего покемона
def test_fragment_of_response():
    response = requests.get('https://pokemonbattle.me:5000/pokemons', params={'pokemon_id': '5307'})
    assert response.json()['name'] == 'Злая тефтелька'

# Проверяем, что в ответе приходит строчка с именем моего тренера и его городом
@pytest.mark.parametrize('key, value', [('trainer_name', 'Valentin'), ('city', 'Portugal')])

# Проверяем параметр ID нашего тренера
def test_parametr(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params={'trainer_id': '2115'})
    assert response.json()[key] == value