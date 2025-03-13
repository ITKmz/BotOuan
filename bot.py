import discord
from modules.config import DISCORD_TOKEN, ALLOWED_CHANNEL_ID
from modules.chat import handle_chat


# กำหนด Intents
intents = discord.Intents.default()
intents.messages = True
intents.voice_states = True  

# สร้างบอท
client = discord.Client(intents=intents)

# ✅ Event เมื่อบอทออนไลน์
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

# ✅ เมื่อมีข้อความในแชท
@client.event
async def on_message(message):
    await handle_chat(client, message)

# รันบอท
client.run(DISCORD_TOKEN)