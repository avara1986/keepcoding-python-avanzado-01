import requests


def get_animal(animal, photo_quality):
    if not animal:
        raise Exception("Animal must be provided")
    if not 0 < photo_quality <= 1080:
        raise Exception("Photo quality must be between 1 and 1080")

    response = requests.get("http://animals.com/api/{animal}".format(animal=animal), params={"quality": photo_quality})
    if not 199 < response.status_code < 300:
        raise Exception("Server did not' want us to have a picture!")
    return response.content
