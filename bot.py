import json
import random
import discord
import openai
import os
from dotenv import load_dotenv
from gtts import gTTS
import asyncio
import imageio_ffmpeg

# โหลด Token จากไฟล์ .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# โหลดข้อความจากไฟล์ boonmathun_core.json
with open("data/boonmathun_core.json", "r", encoding="utf-8") as file:
    core = json.load(file)

# ตั้งค่า Channel ที่ให้บอทตอบ (ใส่ ID ของช่องแชท)
ALLOWED_CHANNEL_ID = 1349123952206942321

# กำหนด Intents สำหรับบอท
intents = discord.Intents.default()
intents.messages = True
intents.voice_states = True  # เพิ่ม voice intents เพื่อให้บอทเข้าห้องเสียง

# สร้างบอท
client = discord.Client(intents=intents)

# ✅ ใช้ FFmpeg ที่ดาวน์โหลดผ่าน imageio
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
discord.FFmpegPCMAudio.executable = ffmpeg_path

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
        return  # อ่านข้อความเฉพาะแชทที่กำหนด

    user_message = message.content
    channel = message.channel

    print(f"👤 {message.author}: {user_message}") # debugging

    # ✅ คำสั่งให้บอทเข้าห้องเสียงเมื่อถูกเรียก "@Ouan เข้าดิส"
    if client.user in message.mentions and "เข้าดิส" in user_message:
        if message.author.voice:  # ตรวจสอบว่าผู้ใช้กำลังอยู่ในห้องเสียง
            channel = message.author.voice.channel
            await channel.connect()
            await message.channel.send("อะกุเข้ามาละ")
        else:
            await message.channel.send("มึงยังไม่เข้าเลย ไอเวร")
        return

    # ✅ คำสั่งให้บอทออกจากห้องเสียงเมื่อถูกเรียก "@Ouan ไปได้แล้ว"
    if client.user in message.mentions and "ไปได้แล้ว" in user_message:
        if message.guild.voice_client:  # ตรวจสอบว่าบอทอยู่ในห้องเสียง
            await message.guild.voice_client.disconnect()
            await message.channel.send("อะๆ กุไปก็ได้")
        else:
            await message.channel.send("กุยังไม่ทันเข้าเลย ไอเวร")
        return

    if client.user in message.mentions:
        # ✅ เพิ่มข้อความของผู้ใช้เข้าไปในประวัติ
        conversation_history.append({"role": "user", "content": user_message})

        # จำกัดความยาวของประวัติ (เช่น 15 ข้อความล่าสุด)
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

            # ✅ ถ้าบอทอยู่ใน Voice Channel ให้พูดออกเสียง
            if message.guild.voice_client:
                await speak_text(message.guild.voice_client, bot_reply)

        except Exception as e:
            print(f"❌ Error: {e}")
            await channel.send(random.choice(core["unknown"]))

# ✅ ฟังก์ชันให้บอทพูด response ใน Voice Channel
async def speak_text(voice_client, text):
    tts = gTTS(text=text, lang="th")  # แปลงข้อความเป็นเสียง
    tts.save("voice.mp3")

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio("voice.mp3"))
        while voice_client.is_playing():
            await asyncio.sleep(1)  # รอให้เสียงเล่นจนจบ

# รันบอท
client.run(DISCORD_TOKEN)
