import requests

# Get for developers ->
# register ->
# API for App ->
# https://developers.giphy.com/explorer/


def get_random_gif_url(search_obj):
    URL = "https://api.giphy.com/v1/gifs/search"

    PARAMETERS = {
        "api_key": "GiFp2ffdGXNciyoQVRTWtMZogRbmzgua",
        "q": search_obj,
        "limit": 1,
        "offset": 0,
        "rating": "g",
        "lang": "en",
        "bundle": "messaging_non_clips",
    }

    response = requests.get(URL, params=PARAMETERS)

    if response.status_code == 200:
        data = response.json()

        if "data" in data and len(data["data"]) > 0:
            gif_url = data["data"][0]["images"]["original"]["url"]
            return gif_url
        else:
            return None
    else:
        return None


def main():
    while True:
        search_obj = input("Write the name of the GIF you want to find: ")
        gif_url = get_random_gif_url(search_obj)

        if gif_url:
            print(f"We found a GIF for you! Link for {search_obj}: {gif_url}")
            break
        else:
            print(f"Sorry, no GIFs found for search '{search_obj}'. Please try again.")


if __name__ == "__main__":
    main()
