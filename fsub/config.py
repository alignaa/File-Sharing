import logging
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = getenv("BOT_TOKEN")
CHANNEL_ID = int(getenv("CHANNEL_ID"))
OWNER = getenv("OWNER")
PROTECT_CONTENT = strtobool(getenv("PROTECT_CONTENT", "False"))
DB_URI = getenv("DATABASE_URL")
FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "0"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "0"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = getenv(
    "START_MESSAGE",
    "<b>🙋🏻‍♂️ʜᴀʟᴏ {mention}!</b>\n\n"
    "<b>ᴛʜᴇ ʙᴏᴛ ɪꜱ ᴜᴘ ᴀɴᴅ ʀᴜɴɴɪɴɢ. ᴛʜᴇꜱᴇ ʙᴏᴛꜱ ᴄᴀɴ ꜱᴛᴏʀᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴄᴜꜱᴛᴏᴍ ᴄʜᴀᴛꜱ, ᴀɴᴅ ᴜꜱᴇʀꜱ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇᴍ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴏᴛ.</b>",
)
FORCE_MSG = getenv(
    "FORCE_MESSAGE",
    "<b>🙋🏻‍♂️ʜᴀʟᴏ {mention}!</b>\n\n"
    "<b>💬 ᴛᴏ ꜱᴇᴇ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛʜᴇ ʙᴏᴛ ɪꜱ ꜱʜᴀʀɪɴɢ, ᴊᴏɪɴ ꜰɪʀꜱᴛ, ᴛʜᴇɴ ᴘʀᴇꜱꜱ ᴛʀʏ ᴀɢᴀɪɴ.</b>"
)
ADMINS = [int(x) for x in (getenv("ADMINS").split())]
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", None)
DISABLE_CHANNEL_BUTTON = getenv("DISABLE_BUTTON", False)

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
