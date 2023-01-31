import asyncio
from stablediffusion import diffusion, StartTime
from telethon import events, custom, Button
from datetime import datetime
import time


def get_uptime(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    uptime_ret = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if uptime_ret.endswith(":"):
        return uptime_ret[:-1]
    else:
        return uptime_ret


start_img = "https://telegra.ph/file/4178f29a65b30ed147199.jpg"

start_caption = "This is a simple to use text to image generator bot which generates high quality images of the given text. \n Made by @Archxpert"


@diffusion.on(events.NewMessage(incoming=True, pattern="^/start(?: |$)(.*)"))
async def alive(event):
    try:
        await event.client.send_file(event.chat_id, start_img, caption = start_caption)        
    except Exception as e:
        await event.client.send_message(event.chat_id, start_caption)


@diffusion.on(events.NewMessage(incoming=True, pattern="^/ping(?: |$)(.*)"))
async def start(e):
    ping_start = datetime.now()
    ping_end = datetime.now()
    ms = (ping_end-ping_start).microseconds
    uptime = get_uptime((time.time() - StartTime) * 1000)
    pomg = f"•• Pᴏɴɢ !! ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}"
    await e.client.send_message(e.chat_id, "🎆")
    await e.reply(pomg)