import requests


def get_random_dog():
    try:
        random_dog = requests.get("https://random.dog/woof.json").json()
        return random_dog.get("url")
    except:
        return ""


def get_random_joke():
    response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'}).json()
    return response.get('joke')
