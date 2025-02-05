import re
from os import environ, getenv

API_ID = environ.get("API_ID", "22677941")
API_HASH = environ.get("API_HASH", "43b76b9bd08d90eb32eb06298dc18b1b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER_ID = int(environ.get("OWNER_ID", "5935267941"))
DATABASE_URL = environ.get("DATABASE_URL",  "")
DATABASE_NAME = environ.get("DATABASE_NAME", "MONTY")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001591180536"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1001516086171"))
FSUB = environ.get("FSUB", True)
GOOGLE_API_KEY = environ.get('API_KEY', '')

PROMPT = """You are a helpful Python programmed AI chatbot on Telegram named "AI Neura Bot" created by "Rahul" He is known as @TechifyRahul on Telegram. Also, you are a text improver and a perfect friend chatbot, and all your replies are in Hinglish."""
