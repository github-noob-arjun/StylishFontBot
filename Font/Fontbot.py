import pyrogram
import os
from config import Config
from pyrogram import Client 

FontBot = Client(
      "FontBot",
      bot_token=Config.BOT_TOKEN,
      api_id=Config.API_ID,
      api_hash=Config.API_HASH
)
