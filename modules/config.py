import os
from dotenv import load_dotenv

# โหลดค่าต่างๆ จาก .env
load_dotenv()

# Token และ API Key
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ตั้งค่า Channel ที่ให้บอทตอบ (ใส่ ID ของช่องแชท)
ALLOWED_CHANNEL_ID = 1349123952206942321