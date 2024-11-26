import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")
APP_ID = int(os.getenv("APP_ID", "19712136"))
API_HASH = os.getenv("API_HASH", "ea41929ce6a602e4293475f030bb91bd")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", ""))
OWNER = os.getenv("OWNER", "excute7")
PROTECT_CONTENT = strtobool(os.getenv("PROTECT_CONTENT", "True"))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", None)
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")
DB_URL = os.getenv("DB_URL", "")
FORCE_SUB_1 = int(os.getenv("FORCE_SUB_1", "0"))
FORCE_SUB_2 = int(os.getenv("FORCE_SUB_2", "0"))
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))
START_MSG = os.getenv(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.getenv("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")
FORCE_MSG = os.getenv(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)
CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", None)
DISABLE_CHANNEL_BUTTON = strtobool(os.getenv("DISABLE_CHANNEL_BUTTON", "False"))
ADMINS.append((1475365115))

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
