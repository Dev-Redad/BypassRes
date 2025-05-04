# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28619924"))
API_HASH = getenv("API_HASH", "f6942e54757244b3971adc66fa0de215")
BOT_TOKEN = getenv("BOT_TOKEN", "7251195381:AAFym-hpv7Zf2xrtU7LRwVu71DKPQY6JheE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7582708769").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Sinchu:Sinchu@sinchu.qwijj.mongodb.net/?retryWrites=true&w=majority&appName=Sinchu")
LOG_GROUP = getenv("LOG_GROUP", -1002567822835)
CHANNEL_ID = int(getenv("CHANNEL_ID", -1002412047920))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
