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

API_ID = int(getenv("API_ID", "25771966"))
API_HASH = getenv("API_HASH", "33039415ffad9db7056892ed652ac1d0")
BOT_TOKEN = getenv("BOT_TOKEN", "7730081012:AAFZ0Y16OwmHK02vLKTG_uVgXhppAEkj8nc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6418117720").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Sinchu:Sinchu@sinchu.qwijj.mongodb.net/?retryWrites=true&w=majority&appName=Sinchu")
LOG_GROUP = getenv("LOG_GROUP", -1002565738939)
CHANNEL_ID = int(getenv("CHANNEL_ID", -1002535991950))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "2"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "20000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
