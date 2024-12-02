import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7968053738:AAEIKNDxn7Q78wdd-Cuvmyv61CIWydPx5r4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28450765"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "36f00f11f9d5c65e69b81fd804453a93")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002314807164"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "sewxiy")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5827289728"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://FileSout:FileSout@cluster0.2d5js.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002118318196"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002423799507"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "300")) # auto delete in seconds

#start message

HELP_TXT = "<b>If you can't use me or don't get any files, it's mean you don't join either <a href=https://t.me/+LGPS4EDPWLA2YTM1>AIO J*v</a> or <a href=https://t.me/AIO_Backup>AIO Backup</a>. First Join These Channels Then retry.</b>"
ABOUT_TXT = "<b>• Creator: <a href=https://t.me/Soutick_09>Soutick</a>\n• Backup Channel: <a href=https://t.me/AIO_Backup>AIO Backup 🔞</a>\n• Best Friend: <a href=tg://settings>This Person</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello!! {mention} 👋! I'm Alya.\n\nI'm here to provide you adult contents for Free 😄\n\n© @AIO_Backup</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5413708222 7272399911").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Bakka ! You're not my Senpai!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5827289728)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
