# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "29113723"))
API_HASH = os.environ.get("API_HASH", "351ac83688f68bf6051091c30995f391")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "AAFniE0UYfn6LuLGPQu3Gacdzx8N50OGm44")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6199578420")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Kapil2Saini")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Kapil2Saini:Kapil@88Krishan@cluster0.43cuqee.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6199578420")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "https://t.me/kpslinkuser")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/Kpslink_official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
