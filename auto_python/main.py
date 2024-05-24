import requests

URL = "https://api.pokemonbattle.me/v2"
TOKEN = "f24b1341738fb541dcfe6d890c4a32fd"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
POKEMON_ID = 28154 #по умолчанию


body_create = {
    "name": "Покемон",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png",
}

body_change = {
    "pokemon_id": str(POKEMON_ID),
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png",
}

body_id = {"pokemon_id": str(POKEMON_ID)}

# Создание покемона
response_create = requests.post(url=f"{URL}/pokemons", headers=HEADER, json=body_create)
POKEMON_ID = response_create.json()["id"]
body_change["pokemon_id"] = str(POKEMON_ID)
body_id["pokemon_id"] = str(POKEMON_ID)
print(response_create.text)

# Смена имени покемона
response_change = requests.put(url=f"{URL}/pokemons", headers=HEADER, json=body_change)
print(response_change.text)

# Поймать в покетбол
response_catch = requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_id)
print(response_catch.text)

# Смена имени тренера
response_change = requests.put(
    url=f"{URL}/trainers", headers=HEADER, json={"name": "TheChamp"}
)
print(response_change.text)
