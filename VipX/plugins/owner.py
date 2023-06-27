from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/00ab5dbe87cd68ab0ef83.jpg",
        caption=f"""cʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙʟᴀᴄᴋ", url=f"https://t.me/UNKNOWN_CRITERIA_RK")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/00ab5dbe87cd68ab0ef83.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʙʟᴀᴄᴋ", url=f"https://t.me/UNKNOWN_CRITERIA_RK")
                ]
            ]
        ),
    )







