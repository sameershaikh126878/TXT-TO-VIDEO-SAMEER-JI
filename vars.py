# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "23480065"))
API_HASH = environ.get("API_HASH", "32edb7d7fc1523b436109bff8ea061fc")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
