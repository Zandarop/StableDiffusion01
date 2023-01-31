import logging
import os
import sys
from inspect import getfullargspec
from os import getenv
from decouple import config
import time
from datetime import datetime
from telethon import TelegramClient, events
from dotenv import load_dotenv


StartTime = time.time()

# logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
OWNER_ID = config("OWNER_ID", cast=int)
Bot_Token = config("Bot_Token", default=None)


print("[INFO]: STARTING TELETHON BOT")

diffusion = TelegramClient('Bot', API_ID, API_HASH).start(bot_token=Bot_Token)