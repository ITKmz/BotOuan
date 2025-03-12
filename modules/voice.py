import os
import discord
import asyncio
from gtts import gTTS
import subprocess
import imageio_ffmpeg

# ✅ ใช้ FFmpeg พาธจาก imageio_ffmpeg
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

# ✅ ตรวจสอบว่า FFmpeg มีไฟล์อยู่จริง
if not os.path.exists(ffmpeg_path):
    raise RuntimeError(f"❌ FFmpeg not found at {ffmpeg_path}")

# ✅ ตรวจสอบว่า FFmpeg ใช้งานได้
try:
    result = subprocess.run([ffmpeg_path, "-version"], capture_output=True, text=True)
    print(f"✅ FFmpeg found at: {ffmpeg_path}\n{result.stdout}")
except Exception as e:
    raise RuntimeError(f"❌ FFmpeg is not working! Error: {e}")

# ✅ กำหนดให้ `discord.py` ใช้ FFmpeg ที่ตรวจสอบแล้ว
os.environ["FFMPEG_BINARY"] = ffmpeg_path
discord.FFmpegPCMAudio.executable = ffmpeg_path

# ✅ กำหนดโฟลเดอร์สำหรับเก็บไฟล์เสียง
AUDIO_FOLDER = "audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# ✅ ให้บอทเข้าห้องเสียง
async def join_voice(message):
    if message.author.voice:
        channel = message.author.voice.channel
        await channel.connect()
        await message.channel.send("อะกุเข้ามาละ")
    else:
        await message.channel.send("มึงยังไม่เข้าเลย ไอเวร")

# ✅ ให้บอทออกจากห้องเสียง
async def leave_voice(message):
    if message.guild.voice_client:
        await message.guild.voice_client.disconnect()
        await message.channel.send("อะๆ กุไปก็ได้")
    else:
        await message.channel.send("กุยังไม่ทันเข้าเลย ไอเวร")

# ✅ ให้บอทพูด response
async def speak_text(voice_client, text):
    audio_path = os.path.join(AUDIO_FOLDER, "voice.mp3")

    tts = gTTS(text=text, lang="th")
    tts.save(audio_path)

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio(audio_path))
        while voice_client.is_playing():
            await asyncio.sleep(1)