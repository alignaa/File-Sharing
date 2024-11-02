import logging
from os import getenv
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = getenv("BOT_TOKEN")
APP_ID = int(getenv("APP_ID"))
API_HASH = getenv("API_HASH")
CHANNEL_ID = int(getenv("CHANNEL_ID"))
OWNER = getenv("OWNER")
PROTECT_CONTENT = strtobool(getenv("PROTECT_CONTENT", "False"))
DB_URI = getenv("DATABASE_URL")
BUTTON_ROW = int(getenv("BUTTON_ROW", 2))
FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1
START_MESSAGE = getenv(
    "START_MESSAGE",
    "<b>🙋🏻‍♂️ʜᴀʟᴏ {mention}!</b>\n\n"
    "<b>ᴛʜᴇ ʙᴏᴛ ɪꜱ ᴜᴘ ᴀɴᴅ ʀᴜɴɴɪɴɢ. ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ᴄᴀɴ ꜱᴛᴏʀᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴄᴜꜱᴛᴏᴍ ᴄʜᴀᴛꜱ, ᴀɴᴅ ᴜꜱᴇʀꜱ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇᴍ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴏᴛ.</b>",
)
FORCE_MESSAGE = getenv(
    "FORCE_MESSAGE",
    "<b>🙋🏻‍♂️ʜᴀʟᴏ {mention}!</b>\n\n"
    "<b>💬 ᴛᴏ ꜱᴇᴇ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛʜᴇ ʙᴏᴛ ɪꜱ ꜱʜᴀʀɪɴɢ, ᴊᴏɪɴ ꜰɪʀꜱᴛ, ᴛʜᴇɴ ᴘʀᴇꜱꜱ ᴛʀʏ ᴀɢᴀɪɴ.</b>"
)
ADMINS = [int(x) for x in (getenv("ADMINS").split())]

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
