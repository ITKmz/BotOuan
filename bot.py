import json
import random
import discord
import openai
import os
from dotenv import load_dotenv

# โหลด Token จากไฟล์ .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ตั้งค่าโฟลเดอร์
DATA_FOLDER = "data"

# โหลดข้อความจากไฟล์ boonmathun_core.json
with open("data/boonmathun_core.json", "r", encoding="utf-8") as file:
    core = json.load(file)

# ตั้งค่า Channel ที่ให้บอทตอบ (ใส่ ID ของช่องแชท)
ALLOWED_CHANNEL_ID = 1349123952206942321

# กำหนด Intents สำหรับบอท
intents = discord.Intents.default()
intents.messages = True

# สร้างบอท
client = discord.Client(intents=intents)

# Event เมื่อบอทออนไลน์
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

# สร้างตัวแปรเก็บประวัติการคุย
conversation_history = []

# Event เมื่อมีข้อความในแชท
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # ไม่ตอบตัวเอง
    
    if message.channel.id != ALLOWED_CHANNEL_ID:
        return  # อ่านข้อความเฉพาะแชท คุยกับอ้วน เท่านั้น

    user_message = message.content
    channel = message.channel

    # print(f"📩 User said: {user_message}")  # Debugging

    # เพิ่มข้อความของผู้ใช้เข้าไปในประวัติ
    conversation_history.append({"role": "user", "content": user_message})

    # จำกัดความยาวของประวัติ (เช่น 10 ข้อความล่าสุด)
    if len(conversation_history) > 15:
        conversation_history.pop(0)

    try:
        # ส่งข้อความไปให้ OpenAI
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": core["system_prompt"]} 
            ] + conversation_history
        )

        # ✅ แก้ไขการเข้าถึงข้อมูล
        if response.choices and response.choices[0].message.content:
            bot_reply = response.choices[0].message.content
        else:
            bot_reply = random.choice(core["unknown"])

        await channel.send(bot_reply)


    except Exception as e:
        print(f"❌ Error: {e}")
        await channel.send(random.choice(core["unknown"]))

# รันบอท
client.run(DISCORD_TOKEN)
