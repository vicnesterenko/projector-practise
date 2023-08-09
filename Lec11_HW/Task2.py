import telebot
import requests

BOT_TOKEN = ""  # my is secret
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


@BOT.message_handler(commands=["start"])
def send_welcome(message):
    BOT.reply_to(message, "Hi dear!💖 Write what gif you want.")


@BOT.message_handler(commands=["find"], func=lambda msg: True)
def search_gif(message):
    search_obj = message.text
    gif_url = get_random_gif_url(search_obj)

    if gif_url:
        BOT.send_message(
            message.chat.id, f"We found a GIF for you! Link for {search_obj}: {gif_url}"
        )
        BOT.send_message(message.chat.id, "Write what gif you want.")
    else:
        BOT.send_message(
            message.chat.id,
            f"Sorry, no GIFs found for search '{search_obj}'. Please try again.",
        )
        BOT.send_message(message.chat.id, "Write what gif you want.")


@BOT.message_handler(commands=["stop"])
def send_welcome(message):
    BOT.reply_to(
        message, "Bye, dear user. See you soon. When you comeback write /start command!"
    )


if __name__ == "__main__":
    BOT.infinity_polling()
