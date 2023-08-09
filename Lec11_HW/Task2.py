import telebot
import requests

BOT_TOKEN = "6453136745:AAFq9CDNwhuq7fBCTJ_Sdm-0vW_HYG6hwsU"

BOT = telebot.TeleBot(BOT_TOKEN)


def get_random_gif_url(search_obj):
    URL = "https://api.giphy.com/v1/gifs/search"
    API_KEY = "GiFp2ffdGXNciyoQVRTWtMZogRbmzgua"

    PARAMETERS = {
        "api_key": API_KEY,
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


@BOT.message_handler(commands=["start", "hello"])
def send_welcome(message):
    BOT.reply_to(message, "Howdy, how are you doing?")


@BOT.message_handler(func=lambda msg: True)
def search_gif(message):
    search_obj = message.text
    gif_url = get_random_gif_url(search_obj)

    if gif_url:
        BOT.send_message(
            message.chat.id, f"We found a GIF for you! Link for {search_obj}: {gif_url}"
        )
    else:
        BOT.send_message(
            message.chat.id,
            f"Sorry, no GIFs found for search '{search_obj}'. Please try again.",
        )


BOT.infinity_polling()
