import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/90b49303716084ccb7f98.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Hello I'm Enmu!** \n\n"
  YUMEKO += "×**I'm Working Properly** \n\n"
  YUMEKO += "×**My Owners : [𝐊𝐨𝐤𝐮𝐬𝐡𝐢𝐛𝐨](https://t.me/UppermoonX1), [Muzan](https://t.me/Demon_xLord)** \n\n"
  YUMEKO += f"×**Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"×**Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "t.me/Enmu_kizuki_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "t.meEnmu_chat_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ENMU,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  YUMEKO = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/EnmuUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)
