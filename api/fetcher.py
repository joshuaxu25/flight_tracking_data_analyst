import requests
from api.config import settings
from project.config import settings
# ROOT_URL = "https://opensky-network.org/api"
ROOT_URL = settings.ROOT_URL
START_DT = project_settings.START_DATE_TIME
END_DT = project_settings.END_DATE_TIME


def states_accessor():
    # Go through Doc API examples
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    # print(r.json())


def tracks_accessor():
    # From reading documentation, running this through is implied first!
    # flights_accessor()
    url = f"{ROOT_URL}/tracks/all?icao24=a808c5&time=1641142800"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    # print(r.json())
    # BUT this is de-activated :(

def flights_accessor():
    url = f"{ROOT_URL}/flights/all?begin=1641142800&end=1641148800"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    return r.json()