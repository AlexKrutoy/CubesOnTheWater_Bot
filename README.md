[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_coding)

[![Static Badge](https://img.shields.io/badge/Telegram-Chat-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_codding_chat)

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/cubesonthewater_bot?start=NzM3ODQ0NDY1)

<img src="https://github.com/AlexKrutoy/CubesOnTheWater_Bot/assets/65369825/7b10981f-6496-4045-b2f7-75bdc78d19f7" width="695" height="425"/>

<img src="https://github.com/AlexKrutoy/CubesOnTheWater_Bot/assets/65369825/a3576803-e335-4e7d-bbc0-3d434e4e5c22" width="695" height="425"/>

## Recommendation before use

# 🔥🔥 Use PYTHON 3.10 🔥🔥

> 🇷 🇺 README in russian available [here](README-RU.md)

## Features  
| Feature                                                     | Supported  |
|---------------------------------------------------------------|:----------------:|
| Multithreading                                                |        ✅        |
| Auto-main blocks                                              |        ✅        |
| Auto-collect boxes from pool                                  |        ✅        |
| Proxy binding to session                                      |        ✅        |
| Support for tdata / pyrogram .session / telethon .session     |        ✅        |


## [Settings](https://github.com/AlexKrutoy/CubesOnTheWater_Bot/blob/main/.env-example/)
| Settings | Description |
|--------------------------|:---------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**    | Platform data from which to run the Telegram session (default - android)                     |
| **TIME_BETWEEN_RECEIVING_BOXES** | Delay between collecting mystery boxes from pool (default [3600, 7200]               |
| **USE_PROXY_FROM_FILE**  | Whether to use a proxy from the bot/config/proxies.txt file (True / False)                   |

## Quick Start 📚

To fast install libraries and run bot - open run.bat on Windows or run.sh on Linux

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the .env file.

## Installation
You can download the [**repository**](https://github.com/AlexKrutoy/CubesOnTheWater_Bot) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/AlexKrutoy/CubesOnTheWater_Bot.git
cd CubesOnTheWater_Bot
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/CubesOnTheWater_Bot >>> python3 main.py --action (1/2)
# Or
~/CubesOnTheWater_Bot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for quick start, for example:
```shell
~/CubesOnTheWater_Bot >>> python main.py --action (1/2)
# Or
~/CubesOnTheWater_Bot >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```



