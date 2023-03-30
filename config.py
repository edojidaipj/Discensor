import os
from dotenv import load_dotenv

load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")
allowed_chars = int(os.environ.get("ALLOWED_NON_JAPANESE_CHARS"))
