import json
import random
import openai
from modules.config import ALLOWED_CHANNEL_ID
from modules.voice import join_voice, leave_voice, speak_text

# โหลดข้อความจากไฟล์ boonmathun_core.json
with open("data/boonmathun_core.json", "r", encoding="utf-8") as file:
    core = json.load(file)

# สร้างตัวแปรเก็บประวัติการคุย
conversation_history = []

# ✅ จัดการข้อความที่บอทต้องตอบ
async def handle_chat(client, message):
    if message.author == client.user:
        return  # ไม่ตอบตัวเอง

    if message.channel.id != ALLOWED_CHANNEL_ID:
        return  # อ่านข้อความเฉพาะแชทที่กำหนด

    user_message = message.content
    channel = message.channel

    # ✅ คำสั่งให้บอทเข้าห้องเสียง
    if client.user in message.mentions and "เข้าดิส" in user_message:
        await join_voice(message)
        return

    # ✅ คำสั่งให้บอทออกจากห้องเสียง
    if client.user in message.mentions and "ไปได้แล้ว" in user_message:
        await leave_voice(message)
        return

    if client.user in message.mentions:
        conversation_history.append({"role": "user", "content": user_message})

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