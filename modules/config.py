import os
from dotenv import load_dotenv

# โหลดค่าต่างๆ จาก .env
load_dotenv()

# Token และ API Key
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ตั้งค่า Channel ที่ให้บอทตอบ (ใส่ ID ของช่องแชท)
ALLOWED_CHANNEL_ID = int(os.getenv("ALLOWED_CHANNEL_ID", "0")) # ถ้าไม่มีค่าให้ใช้ 0 เป็นค่าเริ่มต้น