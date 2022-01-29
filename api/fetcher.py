import requests

def state_fetcher():

    url = f"https://opensky-network.org/api/states/all"
    r = requests.get(url)

    if not r.ok:
        raise RunTimeError(r.json())
    print(r.json)