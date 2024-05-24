import requests
import pytest


URL = "https://api.pokemonbattle.me/v2"
HEADER = {"Content-Type": "application/json"}
TRAINER_ID = "4246"


def test_status_code():
    response = requests.get(url=f"{URL}/trainers")
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(
        url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID}
    )
    print(response_get)
    assert response_get.json()["data"][0]["trainer_name"] == "TheChamp"

