#
# SSH (optional)

`ssh-keygen -t ed25519 -C "github"`

`cat ~/.ssh/id_ed25519.pub`

#
# repo

`git clone git@github.com:UMBARLOCE/phs-tg-bot.git`

#
# venv

`python3 -m venv .venv`

`source .venv/bin/activate`

#
# pip

`pip install --upgrade pip`

`pip install black`

`pip install python-dotenv`

`pip install aiogram`

`pip freeze > requirements.txt`

#
# bot_father

