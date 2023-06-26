from os import getenv
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    # exit("Отсутствует файл .env")
    TG_BOT_TOKEN = input("Введите TOKEN телеграм-бота:\n")
    with open(".env", "w", encoding="utf-8") as file:
        file.write(f"TG_BOT_TOKEN = {TG_BOT_TOKEN}\n")

load_dotenv()

TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")

# headers = {
#     "X-RapidAPI-Key": RAPID_API_KEY,
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }

# base_url = "https://hotels4.p.rapidapi.com/"
