import requests
import json
url = "https://swapi.dev/api/"
responce=requests.get(url).json()
def get_max_diametr(url):
    responce=requests.get(f"https://swapi.dev/api/{url}/").json()
    all_planets=responce.get("results")
    m_result = []
    for planet in all_planets:
        diameter = int(planet.get("diameter"))
        m_result.append(planet.get("diameter"))
    return max(m_result)

get_max_diametr("planets")

def get_max_speed(url):
    responce=requests.get(f"https://swapi.dev/api/{url}/").json()
    all_starships = requests.get("results")
    m_result = []
    for ship in all_starships:
        try:
            speed = int(ship.get("max_atmosphering_speed"))
        except ValueError:
            pass
        m_result.append(speed)
        return max(m_result)
