import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    # exit("Отсутствует файл .env")
    BOT_TOKEN = input("Введите TOKEN телеграм-бота:\n")
    with open(".env", "w", encoding="utf-8") as file:
        file.write(f"BOT_TOKEN = {BOT_TOKEN}\n")

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# headers = {
#     "X-RapidAPI-Key": RAPID_API_KEY,
#     "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }

# base_url = "https://hotels4.p.rapidapi.com/"
