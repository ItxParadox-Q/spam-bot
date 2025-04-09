
from pyrogram import Client, filters
import asyncio
from datetime import datetime, timedelta

api_id = 21162951
api_hash = "cf1c54c75fef54fbbaf96896e070c9f8"
session_name = "fahim"

last_sent = {}

message_text = """
⭕️خریدار گروه های قدیمی شما هستیم :

🚩 ¹|تعداد اعضا و فعالیت گروه مهم نیست
🚩 ²|فقط تاریخ اولین پیام موجود داخل گروه باشه

📍 2023 : برای قیمت پیام بدید
📍2022 ▪️ 550 تومان
📍2021 ▪️ 550 تومان
📍2020 ▪️ 550 تومان
📍2019 ▪️ 550 تومان
📍2018 ▪️ 600 تومان
📍2017 ▪️ 600 تومان
📍2016 ▪️  600 تومان

اگه حتی گروهی بوده که یادتونه داشتید ولی پاکش کردید به من پیام بدید تا راهکاری برای پیدا کردن گروهتون بدم✅

برای فروش به پیوی زیر پیام دهید
@neko_contact
"""

app = Client(session_name, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.me & filters.text & filters.regex(r"(?i)^سلام$"))
async def on_salam(client, message):
    chat_id = message.chat.id
    now = datetime.now()

    if chat_id not in last_sent or now - last_sent[chat_id] > timedelta(minutes=15):
        await client.send_message(chat_id, message_text)
        last_sent[chat_id] = now

app.run()
